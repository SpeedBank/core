import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import BranchInput, BranchUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from accounts.models import Branch, Bank


class BranchNode(DjangoObjectType):
    original_id = graphene.Int()
    latitude = graphene.Float()
    longitude = graphene.Float()
    banner = graphene.String()

    class Meta:
        model = Branch
        exclude_fields = ['location', 'banner']
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id

    def resolve_latitude(self, args, context, info):
        return self.location.latitude

    def resolve_longitude(self, args, context, info):
        return self.location.longitude

    def resolve_banner(self, args, context, info):
        return self.banner.url if self.banner else ""



class CreateBranch(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Branch
    user = False
    input_key = "data"

    class Input:
        data = graphene.Argument(BranchInput)

    branch = graphene.Field(BranchNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(branch=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('bank_id'):
            bank = Bank.objects.get(id=data.get('bank_id'))
            if bank:
                record.bank = bank

        return record


class UpdateBranch(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Branch
    input_key = "data"
    user = False
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(BranchUpdateInput)

    branch = graphene.Field(BranchNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(branch=record, errors=errors)


class DeleteBranch(DeleteNode):
    model = Branch

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    branch = graphene.Field(BranchNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, branch=record)
