from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    context = {"logged_in" : False}
    if request.user.is_authenticated:
        context["user"] = request.user
        context["logged_in"] = True
    return render(request, "landing_page.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials"})

def acct_details(request):
    context = {
        "user": request.user
        }
    return render(request, "acct_details.html", context)

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})
