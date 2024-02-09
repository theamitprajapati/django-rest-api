from django.urls import path
from . import views

urlpatterns = [
  path('',views.welcome),
  path('list',views.list),
  path('register',views.register),
  path('login',views.login),
  path('change_password',views.change_password),

]
   