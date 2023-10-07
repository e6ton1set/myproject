from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from myapp3.models import Author, Post


def hello(request):
    return HttpResponse("It's view-function!")


class HelloView(View):
    @staticmethod
    def get(request):
        return HttpResponse("It's view-Class")


def year_post(request, year):
    res = [1, 2, 3, 4, 5]
    ...
    return HttpResponse(f"Posts from {year}<br> {[num * 2 for num in res]}")


class MonthPost(View):
    def get(self, request, year, month):
        res = [1, 2, 3, 4, 5]
        ...
        return HttpResponse(f"Posts from {month}/{year}<br> {[num * 2 for num in res]}")


def post_detail(request, year, month, slug):
    posts = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python: list() или []",
        "content": "Текст"
    }
    return JsonResponse(posts, json_dumps_params={"ensure_ascii": False})


def my_temp(request):
    context = {"name": "Руслан",
               "content": [1, 2, 3, 4, 5]
               }
    return render(request, "myapp3/my_temp.html", context)


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
                'каждый': 'красный',
                'охотник': 'оранжевый',
                'желает': 'жёлтый',
                'знать': 'зелёный',
                'где': 'голубой',
                'сидит': 'синий',
                'фазан': 'фиолетовый',
            }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/temp_for.html', context)


def index(request):
    return render(request, "myapp3/index.html")


def about(request):
    return render(request, "myapp3/about.html")


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]

    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'myapp3/post_full.html', {'post': post})

