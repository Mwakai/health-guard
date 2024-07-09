from django.contrib.auth import get_user_model
from django.db import models
from config.base_model import BaseModel

User = get_user_model()

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.email

    