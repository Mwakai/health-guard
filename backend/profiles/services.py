from django.shortcuts import get_object_or_404
from .models import Profile
from .serializers import ProfileInputSerializer, ProfileOutputSerilaizer

def profile_create(*, request):

    serialized = ProfileInputSerializer(data=request.data, context={"request": request})

    serialized.is_valid(raise_exception=True)
    profile = Profile.objects.create(**serialized.validated_data)

    return ProfileOutputSerilaizer(profile).data



def profile_update(*, data, user):

    serialized = ProfileInputSerializer(data=data, partial=True)
    serialized.is_valid(raise_exception=True)

    profile = get_object_or_404(Profile, user=user)

    for key, value in serialized.validated_data.items():
        setattr(profile, key, value)

    profile.save()

    return ProfileOutputSerilaizer(profile).data