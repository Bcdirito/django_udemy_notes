from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "level_four_app/index.html")

def other(request):
    return render(request, "level_four_app/other.html")

def relative(request):
    return render(request, "level_four_app/relative_url_templates.html")