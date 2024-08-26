from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import UserCar
from apps.cars.serializers import UserCarSerializer
from rest_framework.permissions import IsAuthenticated


class UserCarCreateListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserCarSerializer
    
    def get_queryset(self):
        return UserCar.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class UserCarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserCarSerializer

    def get_queryset(self):
        return UserCar.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)