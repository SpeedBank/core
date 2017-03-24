import graphene


class CustomerServiceInput(graphene.InputObjectType):
    branch_id = graphene.Int(required=True)
    profile_image = graphene.String(required=False)
    email = graphene.String(required=True)
    phone = graphene.String(required=True)


class CustomerServiceUpdateInput(graphene.InputObjectType):
    profile_image = graphene.String(required=False)
    email = graphene.String(required=False)
    phone = graphene.String(required=False)


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    email = graphene.String(required=True)
    is_active = graphene.Boolean(required=False)
    password = graphene.String(required=True)


class UserUpdateInput(graphene.InputObjectType):
    username = graphene.String(required=False)
    first_name = graphene.String(required=False)
    last_name = graphene.String(required=False)
    email = graphene.String(required=False)
    is_active = graphene.Boolean(required=False)
    password = graphene.String(required=False)
