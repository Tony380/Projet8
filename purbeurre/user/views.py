from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Bienvenu! Votre compte a été créé avec succès! Vous êtes maintenant connecté')
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


class LoginFormView(SuccessMessageMixin, LoginView):
    success_message = "Bienvenu! Vous êtes maintenant connecté"


def logout_view(request):
    logout(request)
    messages.success(request, 'Au revoir! Vous êtes maintenant déconnecté')
    return redirect('index')
