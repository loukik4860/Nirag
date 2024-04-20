from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

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
    form = AuthenticationForm()
    context = {'form': form}
    template_name = 'registration/login.html'
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username= username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"SuccessFully logged in")
                return redirect('')
    return redirect(request,template_name,context)


def registration_success(request):
    return render(request, 'registration/registration_success.html')
