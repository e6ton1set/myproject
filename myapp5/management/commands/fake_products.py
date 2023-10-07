from random import choice, randint
from django.core.management.base import BaseCommand
from myapp5.models import Product, Category


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of products to generate')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get("count")
        for i in range(1, count + 1):
            products.append(Product(
                name=f'Product_{i}',
                category=choice(categories),
                description=f'Description_{i}',
                price=randint(100, 1000),
                quantity=i,
            ))
        Product.objects.bulk_create(products)
        self.stdout.write("success created products")