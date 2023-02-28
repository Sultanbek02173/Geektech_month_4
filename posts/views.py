from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    body = "<h1>Hello</h1>"

    headers = {"name":"Alex",
                "Content-type":"application/vnd.ms-excel",
                "Content-Disposition":"attachment; filename = file.xls"
                }
    return HttpResponse(body, headers = headers, status = 500)


def get_index(request):
    # print(request.user)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else:
    #     return HttpResponse("Не тот запрос")

    context = {
        "title": "Main page",
        "my_list": {1,2,3,4},
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

# Create your views here.
