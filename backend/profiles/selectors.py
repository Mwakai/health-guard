from django.shortcuts import get_object_or_404

from .serializers import ProfileInputSerializer, ProfileOutputSerilaizer
from .models import Profile

def profile_get(*, user):
    profile = get_object_or_404(Profile, user=user)
    serialized = ProfileOutputSerilaizer(profile)
    return serialized.data