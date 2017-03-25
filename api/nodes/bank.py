import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import BankInput, BankUpdateInput
from .shared import GetNodeByUser, CreateUpdateNode, DeleteNode
from accounts.models import Bank


class BankNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = Bank
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateBank(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Bank
    user = False
    input_key = "data"

    class Input:
        data = graphene.Argument(BankInput)

    bank = graphene.Field(BankNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(bank=record, errors=errors)


class UpdateBank(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Bank
    input_key = "data"
    user = False
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(BankUpdateInput)

    bank = graphene.Field(BankNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(bank=record, errors=errors)


class DeleteBank(DeleteNode):
    model = Bank

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    bank = graphene.Field(BankNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, bank=record)
