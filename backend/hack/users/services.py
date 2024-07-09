from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserInputSerializer

def user_create(*, data):

    serialized = UserInputSerializer(data=data)

    serialized.is_valid(raise_exception=True)

    user = User.objects.create_user(**serialized.validated_data)

    token, _ = Token.objects.get_or_create(user=user)

    return {"Token": token.key}

    