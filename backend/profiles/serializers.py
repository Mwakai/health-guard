from rest_framework.serializers import ModelSerializer
from .models import Profile
from hack.users.serializers import UserOutputSerializers

class ProfileInputSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def to_internal_value(self, data):
        if self.context and self.context['request'].method == "POST":
            data['user'] = self.context['request'].user.id
        return super().to_internal_value(data)


class ProfileOutputSerilaizer(ModelSerializer):
    user = UserOutputSerializers()

    class Meta:
        model = Profile
        exclude = ["updated_at"]