from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users/', views.auth_user, name="user"),
    path('create/', views.create_post, name="create"),
]
