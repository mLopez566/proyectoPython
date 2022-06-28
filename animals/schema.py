from dataclasses import fields
from typing import Type
import graphene
from graphene_django import DjangoObjectType

from .models import animal, ranch, upp, raza

class razaType(DjangoObjectType):
    class Meta:
        model = raza
        fields = '__all__'

class uppType(DjangoObjectType):
    class Meta:
        model = upp
        fields = '__all__'

class ranchType(DjangoObjectType):
    class Meta:
        model = ranch
        fields = '__all__'

class animalType(DjangoObjectType):
    class Meta:
        model = animal
        fields = '__all__'


class Query():
    all_animals = graphene.List(animalType)
    all__ranch = graphene.List(ranchType)
    all_upp = graphene.List(uppType)
    all_raza = graphene.List(razaType)

    def resolve_all_animals(root, info):
        return animal.objects.select_related("raza, upp, ranch").all()

    def resolve_all_ranch(root, info):
        return ranch.object.all()

    def resolve_all_upp(root, info):
        return upp.object.all()

    def resolve_all_raza(root, info):
        return raza.object.all()