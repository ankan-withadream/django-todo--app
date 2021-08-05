from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Todos
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required(login_url='/login')
def my_todos(request):
    current_user = request.user
    todos = Todos.objects.filter(username=current_user.username).all()
    context = {'todos':todos}
    if request.method == 'POST':
        titles = request.POST.get('title')
        description = request.POST.get('desc')
        if titles=="" or description=="":
            return redirect("/todos")
        else:
            new_task = Todos(todo_name=titles, username=current_user.username, todo_desc=description)
            new_task.save()
            return redirect("/todos")
    return render(request, "todos.html", context)

@login_required(login_url='/login')
def update(request, tdun):
    current_user = request.user
    todos = Todos.objects.filter(username=current_user.username).all()
    updating = True
    if request.method == "POST":
        if request.POST.get("todo_name")=="" or request.POST.get("todo_desc")=="":
            return redirect(f"/update/{tdun}")
        else:
            todo2be = Todos.objects.filter(todo_name=tdun).first()
            todo2be.todo_name = request.POST.get("todo_name")
            todo2be.todo_desc = request.POST.get("todo_desc")
            todo2be.save()
            return redirect("/todos")
    context = {'todos':todos, 'updating':updating, 'tdun':tdun}    
    return render(request, "todos.html", context)

@login_required(login_url='/login')
def delete(request, tdun):
    todo2be = Todos.objects.filter(todo_name=tdun, username=request.user.username).first()
    todo2be.delete()
    return redirect("/todos")

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username):
            messages.error(request, 'Username you entered, already exists :(')
            return redirect("/signup")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Account created successfully")
            return redirect("/login")
        
    return render(request, "signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username2")
        password = request.POST.get("password2")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully :)")
            return redirect("/todos")
        else:
            messages.error(request, 'Incorrect username or password :(')
            return redirect("/login")
    
    return render(request, "login.html")


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully ")
    return redirect("/login")

