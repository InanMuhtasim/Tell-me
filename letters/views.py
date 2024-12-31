from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Confession
from django.shortcuts import get_object_or_404
from .forms import ConfessionForm


def show_letter(request):
    msg = "Random stuff about us....."
    return render(request, "letter.html", {"message": msg})


def home(request):
    return render(request, "home.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("user-name")
        print(username)
        password = request.POST.get("password")
        print(password)
        try:
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("home")
            else:
                messages.error(request, "User name or password doesn't exist")
        except:
            messages.error(request, "User doesn't exist")

    return render(request, "login.html")


def signUpPage(request):
    if request.method == "POST":
        username = request.POST.get("user-name").lower()
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.error(request, "User Already exists")
        elif password1 != password2:
            messages.error(request, "Passwords doesn't match")
        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email
            )
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("home")

    return render(request, "sign_up.html")


def logoutUser(request):
    logout(request)
    return redirect("home")


def userPage(request):
    user = request.user

    if user.is_authenticated:
        confessions = user.confessions.all()

        return render(
            request, "user_profile.html", {"user": user, "confessions": confessions}
        )
    else:
        return redirect("login")

def confessionPage(request, letter_id):
    confession = get_object_or_404(Confession, letter_id=letter_id)
    if request.COOKIES.get(f"access_{letter_id}") == "granted" or request.user == confession.creator:
        return render(request, "confession.html", {"confession":confession})
    else:
        return redirect("envelop", letter_id=letter_id)

def envelop(request, letter_id):
    if request.method == "POST":
        confession = get_object_or_404(Confession, letter_id=letter_id)
        key = request.POST.get("key")
        if key == confession.key:
            response = redirect("confessionPage", letter_id=letter_id)
            response.set_cookie(f"access_{letter_id}", "granted", max_age=3600)
            return response
        else:
            messages.error(request, "Wrong key")
            return render(request, "envelop.html")
    else:
        return render(request, "envelop.html")

def helpPage(request):
    return render(request, "help.html")
@login_required
def createConfession(request):
    if request.method == "POST":
        form = ConfessionForm(request.POST)
        if form.is_valid():
            confession = form.save(commit=False)
            confession.creator = request.user
            confession.save()
            messages.success(request, "Confession created successfully.")
            return redirect('userPage')
        else:
            messages.error(request, "Both fields are required and cannot be empty.")
    else:
        form = ConfessionForm()

    return render(request, 'confession_form.html', {'form': form, 'type': 'Create'})

@login_required
def updateConfession(request, letter_id):
    confession = get_object_or_404(Confession, letter_id=letter_id)
    
    if confession.creator != request.user:
        messages.error(request, "You are not authorized to edit this confession.")
        return redirect('home')
    
    if request.method == "POST":
        form = ConfessionForm(request.POST, instance=confession)
        if form.is_valid():
            form.save()
            return redirect('userPage')
        else:
            messages.error(request, "Both fields are required and cannot be empty.")
    else:
        form = ConfessionForm(instance=confession)

    return render(request, 'confession_form.html', {'form': form, 'type': 'Update'})

@login_required
def deleteConfession(request, letter_id):
    confession = get_object_or_404(Confession, letter_id=letter_id)

    if confession.creator != request.user:
        messages.error(request, "You are not authorized to delete this confession.")
        return redirect('home')

    if request.method == "POST":
        confession.delete()
        messages.success(request, "Confession deleted successfully.")
        return redirect('home')

    return render(request, 'delete_confirmation.html', {'confession': confession})