from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import UserCar
from apps.cars.serializers import UserCarSerializer


class UserCarCreateListView(ListCreateAPIView):
    serializer_class = UserCarSerializer
    
    def get_queryset(self):
        return UserCar.objects.filter(user_id=self.request.user.pk)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user.id
        return context
    

class UserCarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserCarSerializer

    def get_queryset(self):
        return UserCar.objects.filter(user_id=self.request.user.pk)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user.id
        return context