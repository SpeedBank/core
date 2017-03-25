import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import BankInput, BankUpdateInput
from .shared import GetNodeByUser, CreateUpdateNode, DeleteNode
from accounts.models import Bank


class BankNode(DjangoObjectType):
    original_id = graphene.Int()
    latitude = graphene.Float()
    longitude = graphene.Float()
    logo = graphene.String()
    banner = graphene.String()

    class Meta:
        model = Bank
        exclude_fields = ['location', 'logo', 'banner']
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id

    def resolve_latitude(self, args, context, info):
        return self.location.latitude

    def resolve_longitude(self, args, context, info):
        return self.location.longitude

    def resolve_logo(self, args, context, info):
        return self.logo.url if self.logo else ""

    def resolve_banner(self, args, context, info):
        return self.banner.url if self.banner else ""


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
