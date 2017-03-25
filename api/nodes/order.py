import graphene
from graphene_django import DjangoObjectType

from api.nodes.inputs import OrderInput, OrderUpdateInput
from .shared import CreateUpdateNode, DeleteNode
from accounts.models import Order, Branch, OrderType, BankAccount


class OrderTypeNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = OrderType
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class OrderNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = Order
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateOrder(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Order
    input_key = "data"

    class Input:
        data = graphene.Argument(OrderInput)

    order = graphene.Field(OrderNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(order=record, errors=errors)

    @classmethod
    def perform_extra(cls, record, args):
        data = args.get(cls.input_key)
        if data and data.get('branch_id'):
            branch = Branch.objects.get(id=data.get('branch_id'))
            if branch:
                record.branch = branch

        if data and data.get('bank_account_id'):
            account = BankAccount.objects.get(id=data.get('bank_account_id'))
            if account:
                record.bank_account = account

        if data and data.get('order_type_id'):
            order_type = OrderType.objects.get(id=data.get('order_type_id'))
            if order_type:
                record.order_type = order_type

        return record


class UpdateOrder(CreateUpdateNode, graphene.relay.ClientIDMutation):
    model = Order
    input_key = "data"
    create = False

    class Input:
        id = graphene.String(required=True)
        data = graphene.Argument(OrderUpdateInput)

    order = graphene.Field(OrderNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def result(cls, record, errors={}):
        return cls(order=record, errors=errors)


class DeleteOrder(DeleteNode):
    model = Order

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    order = graphene.Field(OrderNode)

    @classmethod
    def result(cls, deleted, record):
        return cls(deleted=deleted, order=record)
