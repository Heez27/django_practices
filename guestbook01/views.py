from django.shortcuts import render


def index(request):
    return render(request, 'guestbook01/index.html')


def deleteform(request):
    return render(request, 'guestbook01/deleteform.html')

