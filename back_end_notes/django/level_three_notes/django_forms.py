# Django Form Notes

# 3 Advantages
# 1. Quickly generate HTML form widgets with template tagging
# 2. Validate data and process in Python data structure
# 3. Can make form versions of models

# Create forms.py in app directory
# Similiar to creating a model

# Example
from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

# Importing forms to views.py

from . import forms
from forms import FormName

# Example in views.py

def form_name_view(request):
    form = forms.FormName()
    return render(request, "form_name.html", {"form": form})

# Template tagging -> {{ form }}
# No <form> HTML tag
# .as_p returns form template as <p></p> and formats the form
# other .as functions

# csrf_token -> Cross-Site Request Forgery Token that secures the post from false data and the path of data
# Form brakes without tag

# Example:

<div class="container">
    <form method="POST">
        {{ form.as_p }}
        {% csrf_token %}
        <input type="submit" class="btn btn-primary" value="Submit">
    </form>
</div>

# Editing the view:
# .cleaned_data -> Allows pulling data from a dictionary with key/value pairs