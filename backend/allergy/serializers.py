from rest_framework.serializers import ModelSerializer

from .models import Allergy

class AllergyInputSeriaizer(ModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"

class AllergyOutputSeriaizer(ModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"