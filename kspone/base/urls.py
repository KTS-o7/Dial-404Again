from django.urls import path
from . import views

urlpatterns =[
    
    path('login/login', views.loginpage, name="login"),
    path('help/', views.loginhelp, name="help"),
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('fingerprint/', views.fingerprint, name="fingerprint"),
    path('userguide/', views.userguide, name="userguide"),
    path("logout/", views.logoutuser, name = "logout"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

]