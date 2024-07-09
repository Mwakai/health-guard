from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class AllergyView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, user_id):
        pass
