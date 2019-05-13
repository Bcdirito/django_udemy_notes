from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    email = models.EmailField(max_length = 264, unique = True)

# populate database

# confirm through admin interface

# create a view for website for domain extension/users
# users page will be an HTML list of the user names and emails
# use tempalte tags to generate content from User model

# change urls.py to deal with changes to the /users extension