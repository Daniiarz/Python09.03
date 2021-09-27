import datetime
import random

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))


def random_view(request):
    random_int = random.randint(1, 100)
    return HttpResponse(random_int)


def create_blog(request):
    pass


def test_form(request):
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        return HttpResponse(f"ваше имя {first_name} ваша фамилиия {last_name}")
    elif request.method == "GET":
        return render(request, "form.html")
