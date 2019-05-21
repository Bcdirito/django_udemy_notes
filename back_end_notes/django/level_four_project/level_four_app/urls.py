from django.urls import path
from level_four_app import views

# Template Tagging
app_name = "level_four_app"

urlpatterns = [
    path("relative", views.relative, name="relative"),
    path("other", views.other, name="other")
]