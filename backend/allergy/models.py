from django.db import models
from django.contrib.auth import get_user_model
from config.base_model import BaseModel

User = get_user_model()

class Allergy(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
