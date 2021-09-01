from django.urls import path
from . import views
from django.views.generic import ListView


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.index, name='home'),

]