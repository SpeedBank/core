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
from api.nodes.inquiry import (
    InquiryNode, CreateInquiry, UpdateInquiry, DeleteInquiry
)
from api.nodes.customer_service_review import (
    CustomerServiceReviewNode, CreateCustomerServiceReview
)
from api.nodes.branch_review import (
    BranchReviewNode, CreateBranchReview
)
from api.nodes.bank_account_opening import (
    BankAccountOpeningNode, CreateBankAccountOpening, UpdateBankAccountOpening, DeleteBankAccountOpening
)
from api.nodes.discussion import (
    DiscussionNode, CreateDiscussion, DeleteDiscussion
)
from api.nodes.order import (
    OrderNode, CreateOrder, UpdateOrder, DeleteOrder
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

    inquiry = graphene.relay.Node.Field(InquiryNode)
    inquiries = DjangoFilterConnectionField(InquiryNode)

    customer_service_review = graphene.relay.Node.Field(CustomerServiceReviewNode)
    customer_service_reviews = DjangoFilterConnectionField(CustomerServiceReviewNode)

    branch_review = graphene.relay.Node.Field(BranchReviewNode)
    branch_reviews = DjangoFilterConnectionField(BranchReviewNode)

    bank_account_opening = graphene.relay.Node.Field(BankAccountOpeningNode)
    bank_account_openings = DjangoFilterConnectionField(BankAccountOpeningNode)

    discussion = graphene.relay.Node.Field(DiscussionNode)
    discussions = DjangoFilterConnectionField(DiscussionNode)

    order = graphene.relay.Node.Field(OrderNode)
    orders = DjangoFilterConnectionField(OrderNode)


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

    create_inquiry = CreateInquiry.Field()
    update_inquiry = UpdateInquiry.Field()
    delete_inquiry = DeleteInquiry.Field()

    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()

    create_bank_account_opening = CreateBankAccountOpening.Field()
    update_bank_account_opening = UpdateBankAccountOpening.Field()
    delete_bank_account_opening = DeleteBankAccountOpening.Field()

    create_discussion = CreateDiscussion.Field()
    delete_discussion = DeleteDiscussion.Field()

    create_customer_service_review = CreateCustomerServiceReview.Field()
    create_branch_review = CreateBranchReview.Field()
