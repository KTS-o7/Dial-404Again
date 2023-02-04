from django.urls import path
from . import views

urlpatterns = [
    path('login/login', views.loginpage, name="login"),
    path('fingerprint',views.fingerprint,name="fingerprint"),
    path('userguide',views.userguide,name="userguide"),
    path('search',views.search,name="search"),
    path('help/', views.loginhelp, name="help"),
    path('', views.home, name="home"),
    path("logout/", views.logoutuser, name = "logout")


]