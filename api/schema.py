import graphene
from graphene_django.filter import DjangoFilterConnectionField
from api.nodes.user import UserNode, CreateUser, UpdateUser, DeleteUser
from api.nodes.bank import BankNode,CreateBank, UpdateBank, DeleteBank
from api.nodes.branch import BranchNode, CreateBranch, UpdateBranch, DeleteBranch


class Query(graphene.AbstractType):
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    bank = graphene.relay.Node.Field(BankNode)
    banks = DjangoFilterConnectionField(BankNode)

    branch = graphene.relay.Node.Field(BranchNode)
    branches = DjangoFilterConnectionField(BranchNode)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    create_bank = CreateBank.Field()
    update_bank = UpdateBank.Field()
    delete_bank = DeleteBank.Field()

    create_branch = CreateBranch.Field()
    update_branch = UpdateBranch.Field()
    delete_branch = DeleteBranch.Field()
