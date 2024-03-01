from django.contrib.auth.models import User
from rest_framework import generics, permissions  # new

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # new

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # new


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
##Используем ListCreateAPIView, а также IsAuthenticatedOrReadOnly,
# чтобы гарантировать, что аутентифицированные запросы имеют доступ для
# чтения и записи, а неаутентифицированные запросы имеют доступ только
# для чтения.

