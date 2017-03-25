import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import InquiryInput, InquiryUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from services.models import Inquiry
from accounts.models import Bank, Branch


class InquiryNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = Inquiry
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateInquiry(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Inquiry
    input_key = "data"

    class Input:
        data = graphene.Argument(InquiryInput)

    inquiry = graphene.Field(InquiryNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(inquiry=record, errors=errors)

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


class UpdateInquiry(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Inquiry
    input_key = "data"
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(InquiryUpdateInput)

    inquiry = graphene.Field(InquiryNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(inquiry=record, errors=errors)


class DeleteInquiry(DeleteNode):
    model = Inquiry

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    inquiry = graphene.Field(InquiryNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, inquiry=record)
