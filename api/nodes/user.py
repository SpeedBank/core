from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import graphene
from graphene_django import DjangoObjectType

from .utils import get_object, get_errors, load_object, get_load_object
from api.nodes.inputs import UserInput, UserUpdateInput, CustomerServiceInput, CustomerServiceUpdateInput
from accounts.models import CustomerService, Branch
from .shared import GetNodeByUser


class CustomerServiceNode(DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = CustomerService

    def resolve_original_id(self, args, context, info):
        return self.id


class UserNode(GetNodeByUser, DjangoObjectType):
    original_id = graphene.Int()

    class Meta:
        model = User
        filter_fields = {
            'username': ['icontains'],
            'is_active': ['exact']
        }
        filter_order_by = ['id', '-id', 'username', '-username', 'is_active', '-is_active', 'date_joined',
                           '-date_joined']
        interfaces = (graphene.relay.Node, )

    def resolve_original_id(self, args, context, info):
        return self.id


class CreateUser(graphene.relay.ClientIDMutation):

    class Input:
        user_data = graphene.Argument(UserInput)
        customer_service_data = graphene.Argument(CustomerServiceInput)

    user = graphene.Field(UserNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        try:
            user_data = input.get("user_data")
            user = load_object(User(), user_data, ['id', 'password'])
            customer_service_data = input.get("customer_service_data")

            if user_data.get('password'):
                user.set_password(user_data.get('password'))

            user.full_clean()
            user.save()
            if customer_service_data:
                customer_service = load_object(CustomerService(), customer_service_data)
                customer_service.user = user
                branch = Branch.objects.get(id=customer_service_data.get('branch_id'))

                if branch:
                    customer_service.branch = branch
                    customer_service.save()
            return cls(user=user)
        except ValidationError as e:
            return cls(user=None, errors=get_errors(e))


class UpdateUser(graphene.relay.ClientIDMutation):

    class Input:
        id = graphene.String(required=True)
        user_data = graphene.Argument(UserUpdateInput)
        customer_service_data = graphene.Argument(CustomerServiceUpdateInput)

    user = graphene.Field(UserNode)
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):
        user_data = args.get("user_data")
        customer_service_data = args.get("customer_service_data")
        user = get_load_object(User,  args.get('id'), user_data, ['id', 'password'])
        customer_service = CustomerService.objects.get(user=user)
        customer_service = load_object(customer_service, customer_service_data)
        if user_data.get('password'):
            user.set_password(user_data.get('password'))

        try:
            user.full_clean()
            user.save()
            if customer_service:
                customer_service.save()
            return cls(user=user)
        except ValidationError as e:
            return cls(user=None, errors=get_errors(e))


class DeleteUser(graphene.relay.ClientIDMutation):

    class Input:
        id = graphene.String(required=True)

    deleted = graphene.Boolean()
    user = graphene.Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):
        try:
            user = get_object(User, args.get('id'))
            user.delete()
            return cls(deleted=True, user=user)
        except:
            return cls(deleted=False, user=None)
