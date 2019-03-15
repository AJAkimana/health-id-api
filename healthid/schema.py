import graphene
import graphql_jwt

from .apps.authentication.schema import Mutation, Query, ObtainJSONWebToken


class Query(Query, graphene.ObjectType):
    pass
class Mutation(Mutation, graphene.ObjectType):
    # Add Mutations provided by graphql_jwt to generate
    # and verify tokens
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(mutation=Mutation, query=Query)