import graphene


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


class BankInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    logo = graphene.String(required=False)
    banner = graphene.String(required=False)
    address = graphene.String(required=False)
    city = graphene.String(required=False)
    state = graphene.String(required=False)
    country = graphene.String(required=False)
    latitude = graphene.Float(required=False)
    longitude = graphene.Float(required=False)


class BankUpdateInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    logo = graphene.String(required=False)
    banner = graphene.String(required=False)
    address = graphene.String(required=False)
    city = graphene.String(required=False)
    state = graphene.String(required=False)
    country = graphene.String(required=False)
    latitude = graphene.Float(required=False)
    longitude = graphene.Float(required=False)


class BranchInput(graphene.InputObjectType):
    bank_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    sort_code = graphene.Int(required=True)
    banner = graphene.String(required=False)
    email = graphene.String(required=True)
    phone = graphene.String(required=True)
    address = graphene.String(required=False)
    city = graphene.String(required=False)
    state = graphene.String(required=False)
    country = graphene.String(required=False)
    latitude = graphene.Float(required=False)
    longitude = graphene.Float(required=False)


class BranchUpdateInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    sort_code = graphene.Int(required=False)
    banner = graphene.String(required=False)
    email = graphene.String(required=False)
    phone = graphene.String(required=False)
    address = graphene.String(required=False)
    city = graphene.String(required=False)
    state = graphene.String(required=False)
    country = graphene.String(required=False)
    latitude = graphene.Float(required=False)
    longitude = graphene.Float(required=False)


class CustomerServiceInput(graphene.InputObjectType):
    user_id = graphene.String(required=True)
    branch_id = graphene.String(required=True)
    profile_image = graphene.String(required=False)
    email = graphene.String(required=False)
    phone = graphene.String(required=False)


class CustomerServiceUpdateInput(graphene.InputObjectType):
    branch_id = graphene.String(required=False)
    profile_image = graphene.String(required=False)
    email = graphene.String(required=False)
    phone = graphene.String(required=False)


class BankAccountInput(graphene.InputObjectType):
    bank_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    number = graphene.String(required=True)
    phone = graphene.String(required=False)
    email = graphene.String(required=False)
    verified = graphene.Boolean(required=False)


class BankAccountUpdateInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    number = graphene.String(required=False)
    phone = graphene.String(required=False)
    email = graphene.String(required=False)
    verified = graphene.Boolean(required=False)