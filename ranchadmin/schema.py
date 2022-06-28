import graphene

from animals.schema import Query as animalsQuery

class Query(animalsQuery, graphene.ObjectType):
    ping = graphene.String()
    resta = graphene.Float(numx = graphene.Float(), numy = graphene.Float())
    suma = graphene.Float(numx = graphene.Float(), numy = graphene.Float())
    mult = graphene.Float(numx = graphene.Float(), numy = graphene.Float())
    divi = graphene.Float(numx = graphene.Float(), numy = graphene.Float())

    def resolve_ping(root, info):
        return "pong"

    def resolve_resta(root, info, numx, numy):
        return numx - numy
    def resolve_suma(root, info, numx, numy):
        return numx + numy
    def resolve_mult(root, info, numx, numy):
        return numx * numy
    def resolve_divi(root, info, numx, numy):
        return numx / numy

schema = graphene.Schema(query=Query, mutation=None)