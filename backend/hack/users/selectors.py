from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

User = get_user_model()

def user_login(*, request, email, password):
    
    user = authenticate(request, username=email, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return {"Token": token.key}
    else:
        raise AuthenticationFailed("Invalid email or password")
    