from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
path("", views.index, name="home"),
path("signup", views.signup_user, name="signup"),
path("login", views.login_user, name="login"),
path("logout", views.logout_user, name="logout"),

path("todos", views.my_todos, name="my_todos"),
path("update/<str:tdun>", views.update, name="update"),
path("delete/<str:tdun>", views.delete, name="delete")
]

