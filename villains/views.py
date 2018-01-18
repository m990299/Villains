from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .forms import UserForm, LoginForm

from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import VillainForm
from .models import *


def index(request):
    return render(request, "villains/index.html", {})

def test(request):
    return render(request, "villains/default.html", {})

# def register_villain(request):
    # return render(request, "villains/register_villain.html", {})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            return redirect('index')
        else:   
            form = UserForm()
            return render(request, 'registration/adduser.html', {'form':form})

    else:
        form = UserForm()
        return render(request, 'registration/adduser.html', {'form':form})


def register_villain(request):
    if request.method == "POST": #save update_date
        form = VillainForm(request.POST)
        if form.is_valid():
            form.save() #변경내용을 저장
            return redirect('index') #url에 있는 name입력하면 된다

    else:
        form = VillainForm()
        return render(request, "villains/register_villain.html", {"form":form})
