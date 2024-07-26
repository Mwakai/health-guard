from django.urls import path, include
from .views import Register, LogIn

urlpatterns = [
    path("register/", Register.as_view()),
    path("login/", LogIn.as_view()),
    path("my-profile/", include("profiles.urls")),
    path("<str:user_id>/allergies/", include("allergy.urls"))
]
