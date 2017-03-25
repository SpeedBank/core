import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import BankAccountInput, BankAccountUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from accounts.models import BankAccount, Bank


class BankAccountNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = BankAccount
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateBankAccount(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = BankAccount
    input_key = "data"

    class Input:
        data = graphene.Argument(BankAccountInput)

    bank_account = graphene.Field(BankAccountNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(bank_account=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('bank_id'):
            bank = Bank.objects.get(id=data.get('bank_id'))
            if bank:
                record.bank = bank

        return record


class UpdateBankAccount(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = BankAccount
    input_key = "data"
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(BankAccountUpdateInput)

    bank_account = graphene.Field(BankAccountNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(bank_account=record, errors=errors)


class DeleteBankAccount(DeleteNode):
    model = BankAccount

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    bank_account = graphene.Field(BankAccountNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, bank_account=record)
