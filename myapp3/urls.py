from django.urls import path
from myapp3.views import hello, HelloView, year_post, MonthPost, post_detail, view_for, my_temp, index, about
from myapp3.views import author_posts, post_full


urlpatterns = [
    path("hello/", hello, name="hello"),
    path("HelloView/", HelloView.as_view(), name="hello_view"),
    path("posts/<int:year>", year_post, name="year_post"),
    path("posts/<int:year>/<int:month>", MonthPost.as_view(), name="month_post"),
    path("posts/<int:year>/<int:month>/<slug:slug>", post_detail, name="post_detail"),
    path("my_temp/", my_temp, name="my_temp"),
    path("for/", view_for, name="temp_for"),
    path("index/", index, name="index"),
    path("about/", about, name="about"),
    path("author/<int:author_id>", author_posts, name="author_posts"),
    path("post/<int:post_id>", post_full, name="post_full"),
]