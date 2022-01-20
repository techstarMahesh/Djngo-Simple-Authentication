from django.core.checks import messages
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login



from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

# Create your views here.
def index(request):
    # messages.success(request,"This is test massage")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contect = Contect(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contect.save()
        messages.success(request,"Your massage successfully submited")
    return render(request, "index.html")
    # context = {
    #     'variables' : "This is variables",
    # }
    
    # return HttpResponse("This is Homepage")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is About page")


def services(request):
    print(request.user)
    # if request.user.is_anonymous:
    #     return redirect("/login/") 
    return render(request, "services.html")
    # return HttpResponse("This is Services page")

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login/")