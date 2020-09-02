import graphene

import westore.products.schema


class Query(
    westore.products.schema.Query, # Add your Mutation objects here
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(
    westore.products.schema.Mutation, # Add your Mutation objects here
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
