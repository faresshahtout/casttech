from django.shortcuts import render
from django.shortcuts import render, redirect
from forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django import forms
from django.db import IntegrityError


# Create your views here.
def home_page(request):
    formlogin = AuthenticationForm(request, data=request.POST)
    form = NewUserForm(request.POST)
    return render(request=request, template_name="index.html", context={'': ''})


def register_request(request):
    requestsignin=request
    requestsignup=request
    form = NewUserForm(request.POST)
    formlogin = AuthenticationForm(request, data=request.POST)
    context={"register_form":form,"signinform":formlogin}
    which=request.POST.get("Submit")
    print(request.method)
    method="POST" in request.method
    print(request)
    if method:
        if which == "signup":
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    return redirect("/")
                form = NewUserForm()
                return render(request=requestsignup, template_name=r"index.html",
                              context=context)
        if which == "signin":
            if formlogin.is_valid():
                username = formlogin.cleaned_data.get('username')
                password = formlogin.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("http://127.0.0.1:8000/")
                else:
                    messages.error(request, "Invalid username or password.")
                    return render(request=request, template_name=r"index.html",
                                  context=context)
            else:
                messages.error(request, "Invalid username or password.")
                return render(request=request, template_name=r"index.html",
                              context=context)
    return render(request=request, template_name=r"index.html",
                  context=context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


