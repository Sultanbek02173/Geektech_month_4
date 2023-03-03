from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def hello(request):
    body = "<h1>Hello</h1>"

    headers = {"name":"Alex",
                "Content-type":"application/vnd.ms-excel",
                "Content-Disposition":"attachment; filename = file.xls"
                }
    return HttpResponse(body, headers = headers, status = 500)


def get_index(request):
    posts  = Post.objects.filter(status=True)
    # print(request.user)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else:
    #     return HttpResponse("Не тот запрос")

    context = {
        "title": "Main page",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)


def get_contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "posts/contacts.html", context=context)

    # return HttpResponse("Контакты")


def get_about(request):
    context = {
        "title": "Страница о нас"
    }
    return render(request, "posts/about.html", context=context)


def get_post(request):
    posts  = Post.objects.filter(status=True)
    context = {
        "title": "Посты",
        "posts": posts,
    }
    return render(request, "posts/post_create.html", context=context)


def update_post(request):
    posts  = Post.objects.filter(status=True)
    context = {
        "title": "Посты",
        "posts": posts,
    }
    return render(request, "posts/post_update.html", context=context)


def delete_post(request):
    posts  = Post.objects.filter(status=True)
    context = {
        "title": "Посты",
        "posts": posts,
    }
    return render(request, "posts/post_detail.html", context=context)
# Create your views here.
