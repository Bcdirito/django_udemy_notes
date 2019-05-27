from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # **kwargs -> keyword arguments
            # gives corresponding arguments as dictionaries

        # *args -> arguments
            # passes all arguments as a tuple

        context = super().get_context_data(**kwargs)
        context["inject_me"] = "BASIC INJECTION EXAMPLE!"
        return context

class SchoolListView(ListView):
    model = models.School
    template_name = "cbv_app/school_list.html"


class SchoolDetailView(DetailView):
    model = models.School
    template_name = "cbv_app/school_detail.html"


