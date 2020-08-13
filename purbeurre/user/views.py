from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Votre compte à été crée avec succès')
            login(request, user)
            return redirect('index')
        else:
            form = RegisterForm(request.POST)
            return render(request, 'register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')
