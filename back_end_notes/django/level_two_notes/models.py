# Django Models Notes

# Django uses SQLite by default

# Inherits from django.db.models.Model

# Fields have constraints

# Examples:

class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique=True)

class Webpage(models.Model):
    category = models.ForeignKey(Topic)
    name = models.CharField(max_length = 264)
    url = models.URLField()

# To migrate -> input python manage.py migrate

# To make changes -> python manage.py makemigrations app_name

# Must migrate one more time after running makemigrations

# Must register models with admin.py file

# Example:
from django.contrib import admin
from app.models import Model1, Model2
    admin.site.register(Model1)
    admin.site.register(Model2)

# Creating a superuser -> python manage.py createsuperuser
# Then input name, email, and password

# Part Two/Creating Models:

# In Django 2, ForeginKey models require on_delete=models.CASCADE

# To open shell console input python manage.py shell

# To work with an object -> from directory_name.models import Model

# To create a new instance -> same as Rails