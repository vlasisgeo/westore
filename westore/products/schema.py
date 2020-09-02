import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from westore.products.models import Category, Product, Brand

# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'category_products']
        interfaces = (relay.Node, )

class BrandNode(DjangoObjectType):
    class Meta:
        model = Brand
        filter_fields = ['name', 'brand_products']
        interfaces = (relay.Node, )


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
            'brand': ['exact'],
            'brand__name': ['exact', 'icontains', 'istartswith'],

        }
        fields = ("id", "name", "notes", "category", "brand")
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    brand = relay.Node.Field(BrandNode)
    all_brands = DjangoFilterConnectionField(BrandNode)

    product = relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)



class ProductMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        notes = graphene.String(required=True)
        
        id = graphene.ID()

    # The class attributes define the response of the mutation
    product = graphene.Field(ProductNode)

    def mutate(self, info, notes, id):
        product = ProductNode.objects.get(pk=id)
        product.notes = notes
        product.save()
        # Notice we return an instance of this mutation
        return ProductMutation(product=product)


class Mutation(graphene.ObjectType):
    update_product = ProductMutation.Field()