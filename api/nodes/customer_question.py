import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import CustomerQuestionInput, CustomerQuestionUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from services.models import CustomerQuestion
from accounts.models import Bank


class CustomerQuestionNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = CustomerQuestion
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateCustomerQuestion(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = CustomerQuestion
    input_key = "data"

    class Input:
        data = graphene.Argument(CustomerQuestionInput)

    customer_question = graphene.Field(CustomerQuestionNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(customer_question=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('bank_id'):
            bank = Bank.objects.get(id=data.get('bank_id'))
            if bank:
                record.bank = bank

        return record


class UpdateCustomerQuestion(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = CustomerQuestion
    input_key = "data"
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(CustomerQuestionUpdateInput)

    customer_question = graphene.Field(CustomerQuestionNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(customer_question=record, errors=errors)


class DeleteCustomerQuestion(DeleteNode):
    model = CustomerQuestion

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    customer_question = graphene.Field(CustomerQuestionNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, customer_question=record)
