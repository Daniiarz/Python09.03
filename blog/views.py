import datetime
import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Blog, Comment


def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))


def random_view(request):
    random_int = random.randint(1, 100)
    return HttpResponse(random_int)


class CreateBlogView(CreateView):
    model = Blog
    template_name = "blog_form.html"
    fields = [
        "image",
        "title",
        "description",
    ]


class BlogListView(ListView):
    queryset = Blog.objects.all()
    template_name = "blog.html"
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    template_name = "blog_detail.html"
    context_object_name = "blog"
    pk_url_kwarg = "id"

    # ДЗ
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        pass


def detail_post(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        text = request.POST.get("comment", None)
        if not text:
            comments = Comment.objects.filter(blog_id=id)
            return render(request, "blog_detail.html", context={"blog": blog, "comments": comments})
        else:
            Comment.objects.create(text=text, blog=blog)
            comments = Comment.objects.filter(blog_id=id)
            return render(request, "blog_detail.html", context={"blog": blog, "comments": comments})
    elif request.method == "GET":
        comments = Comment.objects.filter(blog_id=id)
        return render(request, "blog_detail.html", context={"blog": blog, "comments": comments})


def profile_view(request):
    user = request.user
    return HttpResponse(f"username: {user.username}, password: {user.password}, name: {user.first_name}, surname: {user.last_name}")


def blog_change_view(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        file = request.FILES
        if data.get("title"):
            blog.title = data["title"]
        if data.get("description"):
            blog.description = data["description"]
        if file.get("image"):
            blog.image = file["image"]
        blog.save()
        return HttpResponseRedirect(f"/blog/{blog.id}")
    elif request.method == "GET":
        context = {"blog": blog}
        return render(request, "blog_change.html", context)


@api_view(['GET'])
def rest_view(request):
    data = {
        "username": "maruf_10_offial",
        "password": "Qwerty!123",
    }
    return Response(data)
