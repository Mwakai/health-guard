from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .services import user_create
from .selectors import user_login
from .serializers import UserLogInSerializer

class Register(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        tokenObj = user_create(data=request.data)
        
        return Response(tokenObj, status.HTTP_201_CREATED)


class LogIn(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serialized = UserLogInSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)

        tokenObj = user_login(request=request, **serialized.validated_data)

        return Response(tokenObj, status.HTTP_200_OK)
