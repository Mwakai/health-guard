from django.urls import path
from .views import AllergyView

urlpatterns = [
    path("", AllergyView.as_view())
]