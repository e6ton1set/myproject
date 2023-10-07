from django.urls import path
from myapp5.views import total_in_db, total_in_view, total_in_template

urlpatterns = [
    path("db/", total_in_db, name="total_in_db"),
    path("view/", total_in_view, name="total_in_view"),
    path("templates/", total_in_template, name="total_in_template"),
]