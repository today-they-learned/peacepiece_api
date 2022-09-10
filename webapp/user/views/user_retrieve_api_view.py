from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from user.serializers import UserSerializer

User = get_user_model()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
