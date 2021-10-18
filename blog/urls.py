from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_view),
    path("<int:id>", views.detail_post),
    path("<int:id>/change", views.blog_change_view),
    path("hello-world", views.date_view),
    path("random", views.random_view),
    path("form", views.test_form),
    path("create", views.create_blog),
    path("profile", views.profile_view),
    path("rest", views.rest_view)
]
