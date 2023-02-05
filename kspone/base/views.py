from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .pdf import html2pdf
from .models import Ksp
from django.db import connection, reset_queries
import psycopg2
# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
                
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or password error")
    context = {}
    return render(request, 'loginpage.html', context)
def logoutuser(request):
     logout(request)
     return redirect("login")
def loginhelp(request):

        context = {}
        return render(request, 'loginhelp.html', context)

@login_required(login_url='login/login')
def home(request):
     context = {}
     return render(request, 'home.html', context)
def search(request):
      context = {}
      return render(request, 'search.html', context)
def fingerprint(request):
      context = {}
      return render(request, 'fingerprint.html', context)
def userguide(request):
      context = {}
      return render(request, 'userguide.html', context)
def pdf(request):
     pdf = html2pdf("pdf.html")
     return HttpResponse(pdf, content_type="application/pdf")


def state(request):
    results = ksp.objects.all()
    if request.method == 'POST':
        state = request.POST.get('state')
        results = Ksp.objects.all()
        content = {'results': results, 'state': state}
        return render(request, 'search.html', content)

    content = {'results': results}
    return render(request, 'search.html', content)

# def state(request):
    # conn = psycopg2.connect(
    # host="kspone.postgres.database.azure.com",
    # database="police",
    # user="mykspadmin",
    # password="PoliceHackathon123",
    # port="5432"
    #     )
    # cur = conn.cursor()
    # cur.execute("SELECT person_name FROM icjs WHERE state = 'Karnataka'")
    # results = cur.fetchall()
    # content = {'results': results}
    # return render(request, 'search.html', content)

    #     state = request.POST.get("state")
    #     print(state)
    #
    #     if state:
    #         with connection.cursor() as cursor:
    #             cursor.execute("SELECT person_name FROM icjs WHERE state = 'Karnataka'")
    #             results = cursor.fetchall()
    #             print(results)
    #         return render(request, "search.html", {"results": results})
    # return render(request, "search.html")


