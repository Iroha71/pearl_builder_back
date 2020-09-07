from os import write
from pyexpat import model
from django.contrib.auth import update_session_auth_hash
from django.template.context_processors import request
from pkg_resources import require
from rest_framework import serializers
from .models import Account, AccountManager

class AccountSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=False)

  class Meta:
    model = Account
    fields = ('id', 'username', 'password')

  def create(self, validated_data):
    return Account.objects.create_user(request_data=validated_data)