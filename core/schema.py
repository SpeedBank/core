import graphene

from api import schema as api_schema


class Query(api_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=api_schema.Mutation)
