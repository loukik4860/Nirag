from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def registerVeiw(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Has been successfully Created')
            return redirect('registration_success')  # Redirect to a success page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def loginView(request):
    template_name = "registration/login.html"
    context = {}
    if request.method == "POST":
        uname = request.POST.get('username')
        print(uname)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=uname, password=password)
        print("----------------", user)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('registration_success')
        else:
            messages.error(request, 'User credentials are not correct')
    return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('login')


def registration_success(request):
    return render(request, 'registration/registration_success.html')
