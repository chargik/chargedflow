from rest_framework import generics

from leads.models import Join
from .serializers import JoinSerializer


class JoinCreateAPIView(generics.CreateAPIView):
    queryset = Join.objects.all()
    serializer_class = JoinSerializer
    permission_classes = []
    authentication_classes = []

    # def perform_create(self, serializer):
    #     serializer.save(url_field=self.request.path)
    #     print(self.request.path)