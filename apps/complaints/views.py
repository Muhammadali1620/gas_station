from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.complaints.models import Complaint
from apps.complaints.serializers import ComplaintCreateSerializer


class ComplaintCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ComplaintCreateSerializer

