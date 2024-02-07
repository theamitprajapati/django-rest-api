from django.urls import path

from . import views

from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
  path('',views.welcome),
  path('list',views.list),
  path('register',views.register),
  path('login',views.login),
 path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
   