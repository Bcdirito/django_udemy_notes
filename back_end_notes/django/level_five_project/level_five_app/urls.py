from django.urls import path
from level_five_app import views

app_name = "level_five_app"

urlpatterns = [
    path("register", views.register, name="register")
]
