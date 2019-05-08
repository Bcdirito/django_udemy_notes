# Create Application Notes

# To create application input python project_directory/manage.py startapp application_name

# __init__.py:
# Same as project

# admin.py:
# Can register models with admin interface

# apps.py:
# Application specific config

# models.py:
# Store data models

# test.py:
# Store test functions

# views.py:
# Handle requests and responses

# Migrations Folder:
# Stores database info in relation to models

# To register the creation of an app, add it to settings.py file in the INSTALLED_APPS list

# To Create a View:
# In application_name/views.py:
# input from django.http import HttpResponse
# Each view must return HttpResponse

# Mapping Views to URL:
# In urls.py add path("route", views.function_name,name="function_name")
