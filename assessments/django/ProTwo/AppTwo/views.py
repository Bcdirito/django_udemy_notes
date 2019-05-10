from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    help_heading = {
        "heading": "THIS IS THE HELP PAGE!"
    }

    return render(request, "app_two/help.html", context=help_heading)