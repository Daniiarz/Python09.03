from django.urls import path
from .views import date_view, random_view, test_form

urlpatterns = [
    path("hello-world", date_view),
    path("random", random_view),
    path("form", test_form)
]
