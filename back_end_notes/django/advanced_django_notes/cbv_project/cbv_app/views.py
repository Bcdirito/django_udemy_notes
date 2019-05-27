from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
     # returns school_list -> list of school objects

    context_object_name = "schools"
    template_name = "cbv_app/school_list.html"


class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = "school_detail"
    template_name = "cbv_app/school_detail.html"

class SchoolCreateView(CreateView):
    model = models.School
    template_name = "cbv_app/school_form.html"
    fields = ("name", "principal", "location")

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ("name", "principal")

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url =  reverse_lazy("cbv_app:list")