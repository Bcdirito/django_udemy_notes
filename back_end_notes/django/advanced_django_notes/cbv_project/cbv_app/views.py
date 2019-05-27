from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

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


