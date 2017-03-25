import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import FaqInput, FaqUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from services.models import Faq
from accounts.models import Bank


class FaqNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = Faq
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateFaq(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Faq
    user = False
    input_key = "data"

    class Input:
        data = graphene.Argument(FaqInput)

    faq = graphene.Field(FaqNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(faq=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('bank_id'):
            bank = Bank.objects.get(id=data.get('bank_id'))
            if bank:
                record.bank = bank

        return record


class UpdateFaq(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Faq
    input_key = "data"
    user = False
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(FaqUpdateInput)

    faq = graphene.Field(FaqNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(faq=record, errors=errors)


class DeleteFaq(DeleteNode):
    model = Faq

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    faq = graphene.Field(FaqNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, faq=record)
