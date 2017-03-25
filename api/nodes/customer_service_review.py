import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import CustomerServiceReviewInput
from .shared import CreateUpdateNode
from accounts.models import CustomerServiceReview, CustomerService


class CustomerServiceReviewNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = CustomerServiceReview
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateCustomerServiceReview(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = CustomerServiceReview
    user = False
    input_key = "data"

    class Input:
        data = graphene.Argument(CustomerServiceReviewInput)

    customer_service_review = graphene.Field(CustomerServiceReviewNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(customer_service_review=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('customer_service_id'):
            customer_service = CustomerService.objects.get(id=data.get('customer_service_id'))
            if customer_service:
                record.customer_service = customer_service

        return record
