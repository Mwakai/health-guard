from django.urls import path, include
from .views import Profile

urlpatterns = [
    path("", Profile.as_view())
]