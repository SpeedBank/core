import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

from api.nodes.inputs import DiscussionInput
from .shared import CreateUpdateNode, DeleteNode
from services.models import Discussion, Inquiry


class DiscussionNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = Discussion
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateDiscussion(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Discussion
    input_key = "data"

    class Input:
        data = graphene.Argument(DiscussionInput)

    discussion = graphene.Field(DiscussionNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(discussion=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('recipient_id'):
            recipient = User.objects.get(id=data.get('recipient_id'))
            if recipient:
                record.recipient = recipient

        if data and data.get('inquiry_id'):
            inquiry = Inquiry.objects.get(id=data.get('inquiry_id'))
            if inquiry:
                record.inquiry = inquiry

        return record


class DeleteDiscussion(DeleteNode):
    model = Discussion

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    discussion = graphene.Field(DiscussionNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, discussion=record)
