from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person


# получения данных из БД

def index(request):
    # people = Person.objects.all()
    return render(request, "blog/index.html")


def base(request):
    # people = Person.objects.all()
    return render(request, "base.html")


def adbout(request):
    # people = Person.objects.all()
    return render(request, "adbout.html")


def news(request):
    # people = Person.objects.all()
    return render(request, "news.html")


def banner(request):
    # people = Person.objects.all()
    return render(request, "blog/banner.html", context={'info_1': 'HTML'})



# сохранения данных в БД
"""
В функцию create() получаем данные из запроса типа POST,
сохраняем данные с помощью метода save() и выполняем переадресацию на 
корень сайта (на index.html) 
"""


def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")


# изменение данных в БД

def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == 'POST':
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")

        else:
            return render(request, "blog/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2> Person not found</h2>")


# Удаления данных из БД

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2> Person not found</h2>")


"""
Токен CSRF — это безопасный случайный токен (например, токен синхронизатора или токен 
вызова), который используется для предотвращения атак CSRF. 
Токен должен быть уникальным для каждого сеанса пользователя и иметь 
большое случайное значение, чтобы его было трудно угадать. Приложение с защитой 
CSRF назначает уникальный токен CSRF для каждого сеанса пользователя.
"""
