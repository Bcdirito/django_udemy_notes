from django.shortcuts import render
from django.http import HttpResponse
# from AppTwo.models import User
from .forms import NewUserForm

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome!</h1><h2> Go to /users to see the list of user information!</h2>")

def help(request):
    help_heading = {
        "heading": "THIS IS THE HELP PAGE!"
    }

    return render(request, "app_two/help.html", context=help_heading)

def users(request):
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return help(request)
        else:
            print("ERROR FORM INVALID")
    
    return render(request, "app_two/users.html", {"form": form})