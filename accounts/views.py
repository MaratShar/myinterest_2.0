from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from wall.models import Image, Like

def login_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        password_1 = request.POST["password_1"]
        try:
            user = authenticate(username = name, password = password_1)
            login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        except:
            error_message = "User was not found"
            return render(request, "accounts/login.html", {"error_message": error_message})
    return render(request, "accounts/login.html")

def profile_view(request):
    my_photo = Image.objects.filter(author = request.user)
    liked_photo = Like.objects.filter(user = request.user)
    content = {}
    content["images"] = my_photo
    content["liked_images"] = liked_photo
    return render(request, "accounts/profile.html", content)

def register_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]
        if password_1 == password_2:
            try:
                user = User.objects.create_user(username = name, password = password_1)
                return HttpResponseRedirect(reverse("login"))
            except:
                error_message = "Can not create user."
                return render(request, "accounts/register.html", {"error_message": error_message})
        else:
            error_message = "Passwords are different."
            return render(request, "accounts/register.html", {"error_message": error_message})
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("wall"))