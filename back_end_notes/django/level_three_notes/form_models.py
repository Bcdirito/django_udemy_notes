# Form Model Notes

# Example:
from django import forms
from myapp.models import MyModel

class MyNewForm(forms.ModelForm):
    # You have to pass in form fields if you want custom validators
    class Meta:
        model = MyModel
        fields = "__all__"
        # grabs all fields from model and places in form

        # option 2:
        # exclude = ["field1", "field2"]

        # option 3:
        # fields = ("field1", "field2")