from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.views import View

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
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return FileResponse(result, content_type='application/pdf')
    return None
data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('C:\Users\sarang\Desktop\Dial-404\kspone\HTML\index.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('C:\Users\sarang\Desktop\Dial-404\kspone\HTML\index.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
def index(request):
	context = {}
	return render(request, 'C:\Users\sarang\Desktop\Dial-404\kspone\HTML\index.html', context)

