import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import BankAccountOpeningInput, BankAccountOpeningUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from accounts.models import BankAccountOpening, Bank, Branch


class BankAccountOpeningNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = BankAccountOpening
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateBankAccountOpening(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = BankAccountOpening
    input_key = "data"

    class Input:
        data = graphene.Argument(BankAccountOpeningInput)

    bank_account_opening = graphene.Field(BankAccountOpeningNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(bank_account_opening=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('bank_id'):
            bank = Bank.objects.get(id=data.get('bank_id'))
            if bank:
                record.bank = bank

        if data and data.get('branch_id'):
            branch = Branch.objects.get(id=data.get('branch_id'))
            if branch:
                record.branch = branch

        return record


class UpdateBankAccountOpening(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = BankAccountOpening
    input_key = "data"
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(BankAccountOpeningUpdateInput)

    bank_account_opening = graphene.Field(BankAccountOpeningNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(bank_account_opening=record, errors=errors)


class DeleteBankAccountOpening(DeleteNode):
    model = BankAccountOpening

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    bank_account_opening = graphene.Field(BankAccountOpeningNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, bank_account_opening=record)
