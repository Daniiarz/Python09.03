from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view()),
    path("<int:id>", views.BlogDetailView.as_view()),
    path("<int:id>/change", views.blog_change_view),
    path("hello-world", views.date_view),
    path("random", views.random_view),
    path("create", views.CreateBlogView.as_view()),
    path("profile", views.profile_view),
    path("rest", views.rest_view)
]
