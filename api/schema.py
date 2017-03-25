import graphene
from graphene_django.filter import DjangoFilterConnectionField
from api.nodes.user import UserNode, CreateUser, UpdateUser, DeleteUser
from api.nodes.bank import BankNode,CreateBank, UpdateBank, DeleteBank
from api.nodes.branch import BranchNode, CreateBranch, UpdateBranch, DeleteBranch
from api.nodes.customer_service import (
    CustomerServiceNode, CreateCustomerService, UpdateCustomerService, DeleteCustomerService
)
from api.nodes.bank_account import (
    BankAccountNode, CreateBankAccount, UpdateBankAccount, DeleteBankAccount
)
from api.nodes.faq import (
    FaqNode, CreateFaq, UpdateFaq, DeleteFaq
)
from api.nodes.customer_question import (
    CustomerQuestionNode, CreateCustomerQuestion, UpdateCustomerQuestion, DeleteCustomerQuestion
)


class Query(graphene.AbstractType):
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    bank = graphene.relay.Node.Field(BankNode)
    banks = DjangoFilterConnectionField(BankNode)

    branch = graphene.relay.Node.Field(BranchNode)
    branches = DjangoFilterConnectionField(BranchNode)

    customer_service = graphene.relay.Node.Field(CustomerServiceNode)
    customer_services = DjangoFilterConnectionField(CustomerServiceNode)

    bank_account = graphene.relay.Node.Field(BankAccountNode)
    bank_accounts = DjangoFilterConnectionField(BankAccountNode)

    faq = graphene.relay.Node.Field(FaqNode)
    faqs = DjangoFilterConnectionField(FaqNode)

    customer_question = graphene.relay.Node.Field(CustomerQuestionNode)
    customer_questions = DjangoFilterConnectionField(CustomerQuestionNode)


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

    create_customer_service = CreateCustomerService.Field()
    update_customer_service = UpdateCustomerService.Field()
    delete_customer_service = DeleteCustomerService.Field()

    create_bank_account = CreateBankAccount.Field()
    update_bank_account = UpdateBankAccount.Field()
    delete_bank_account = DeleteBankAccount.Field()

    create_faq = CreateFaq.Field()
    update_faq = UpdateFaq.Field()
    delete_faq = DeleteFaq.Field()

    create_customer_question = CreateCustomerQuestion.Field()
    update_customer_question = UpdateCustomerQuestion.Field()
    delete_customer_question = DeleteCustomerQuestion.Field()
