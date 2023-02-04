

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import FileResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa


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
def  fingerprint(request):
    context= {}
    return render(request,'fingerprint.html',context)    
def  userguide(request):
    context= {}
    return render(request,'userguide.html',context) 
def  search(request):
    context= {}
    return render(request,'search.html',context)     

def search_results(request):
  query = request.GET.get('q')
  filter1 = request.GET.get('filter1')
  filter2 = request.GET.get('filter2')
  filter3 = request.GET.get('filter3')

  # Code to fetch data from Django models based on the filters selected
  # ...

  return render(request, 'search_results.html', {'query': query, 'filter1': filter1, 'filter2': filter2, 'filter3': filter3})
def generate_pdf(request):
    template = get_template('pdf_template.html')
    html = template.render({})
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return FileResponse(result, content_type='application/pdf')
    return None   