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
    print(request.user)
    if request.method == "GET":
        return HttpResponse("Главная страница")
    else:
        return HttpResponse("Не тот запрос")


def get_contacts(request):
    return HttpResponse("Контакты")


def get_about(request):
    return HttpResponse("Данные")

# Create your views here.
