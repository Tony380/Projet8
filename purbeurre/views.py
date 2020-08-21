from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def legal(request):
    return render(request, 'legal.html')


def my_404_view(request, exception):
    return render(request, '404.html')


def my_500_view(request):
    return render(request, '500.html')
