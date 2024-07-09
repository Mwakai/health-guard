from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .selectors import profile_get
from .services import profile_create, profile_update

class Profile(APIView):

    def get(self, request):
        profile = profile_get(user=request.user)
        if profile:
            return Response(profile, status.HTTP_200_OK)
        return Response({"detail": "Not foud"}, status.HTTP_404_NOT_FOUND)

    def post(self, request):
        profile = profile_create(request=request)
        if profile:
            return Response(profile, status.HTTP_201_CREATED)
        return Response({"detail": "An error occured"}, status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        #TODO: Does not change profile's user
        
        profile = profile_update(data=request.data, user=request.user)
        if profile:
            return Response(profile, status.HTTP_200_OK)   #TODO: Change stATUS code
        return Response({"detail": "An error occured"}, status.HTTP_400_BAD_REQUEST)