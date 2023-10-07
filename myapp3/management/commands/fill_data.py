from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicingelit. " \
        "Accusamus accusantium aut beatae consequatur consequuntur cumque, " \
        "delectus et illo iste maxime nihil non nostrum odio officia, " \
        "perferendis placeat quasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpaducimus, " \
        "eaque eum illo mollitia nemo tempore unde vero! Blanditiis deleniti ex hic"


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of User')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=32)),
                    author=author
                )
                post.save()
        self.stdout.write("success")