import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import CustomerServiceInput, CustomerServiceUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from accounts.models import CustomerService, Branch


class CustomerServiceNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = CustomerService
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateCustomerService(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = CustomerService
    input_key = "data"

    class Input:
        data = graphene.Argument(CustomerServiceInput)

    customer_service = graphene.Field(CustomerServiceNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(customer_service=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('branch_id'):
            branch = Branch.objects.get(id=data.get('branch_id'))
            if branch:
                record.branch = branch

        return record


class UpdateCustomerService(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = CustomerService
    input_key = "data"
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(CustomerServiceUpdateInput)

    customer_service = graphene.Field(CustomerServiceNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(customer_service=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('branch_id'):
            branch = Branch.objects.get(id=data.get('branch_id'))
            if branch:
                record.branch = branch

        return record


class DeleteCustomerService(DeleteNode):
    model = CustomerService

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    customer_service = graphene.Field(CustomerServiceNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, customer_service=record)
