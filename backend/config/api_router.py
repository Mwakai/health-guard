from django.urls import path, include

urlpatterns = [
    path("users/", include("hack.users.urls")),
]
