import graphene
from graphene_django import DjangoObjectType

from accounts.models import OrderType


class OrderTypeNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = OrderType
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id