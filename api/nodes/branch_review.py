import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import BranchReviewInput
from .shared import CreateUpdateNode
from accounts.models import BranchReview, Branch


class BranchReviewNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = BranchReview
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateBranchReview(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = BranchReview
    user = False
    input_key = "data"

    class Input:
        data = graphene.Argument(BranchReviewInput)

    branch_review = graphene.Field(BranchReviewNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(branch_review=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('branch_id'):
            branch = Branch.objects.get(id=data.get('branch_id'))
            if branch:
                record.branch = branch

        return record
