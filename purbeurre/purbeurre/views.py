from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def legal(request):
    return render(request, 'legal.html')
