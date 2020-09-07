from os import stat
from django.db.migrations import serializer
from django.template.context_processors import request
from rest_framework.response import Response
from django.db import transaction
from rest_framework import authentication, permissions, generics, status
from .serializers import AccountSerializer
from django.contrib.auth import get_user_model

# Create your views here.
class AuthRegister(generics.CreateAPIView):
  Account = get_user_model()
  permission_classes = (permissions.AllowAny,)
  queryset = Account.objects.all()
  serializer_class = AccountSerializer

  @transaction.atomic
  def post(self, request, format=None):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthInfoGetView(generics.RetrieveAPIView):
  Account = get_user_model()
  permission_classes = (permissions.IsAuthenticated)
  queryset = Account.objects.all()
  serializer_class = AccountSerializer

  def get(self, request, format=None):
    return Response(data={
      'username': request.user.username
    },
    status=status.HTTP_200_OK)