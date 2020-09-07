from pyexpat import model
from django.db import models
from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.
class AccountManager(BaseUserManager):
  def create_user(self, request_data, **kwargs):
    now = timezone.now()
    if not request_data['username']:
      raise ValueError('Users must have an username')

    user = self.model(
      username = request_data['username'],
      is_active = True,
      last_login = now,
      date_joined = now,
    )
    user.set_password(request_data['password'])
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email, password, **extra_fields):
    request_data = {
      'username': username,
      'password': password
    }
    user = self.create_user(request_data)
    user.is_active = True
    user.is_staff = True
    user.is_admin = True
    user.save(using=self._db)
    return user

class Account(AbstractBaseUser):
  username = models.CharField(_('username'), max_length=30, unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  last_login = models.DateTimeField(default=timezone.now)
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

  objects = AccountManager()

  USERNAME_FIELD = 'username'

  def user_has_perm(user, perm, obj):
    return _user_has_perm(user, perm, obj)
  
  def has_perm(self, perm, obj=None):
    return _user_has_perm(self, perm, obj=obj)

  def has_module_perms(self, app_label):
    return self.is_admin
  
  def get_short_name(self):
    return self.username

  @property
  def is_superuser(self):
    return self.is_admin
  
  # class Meta:
  #   db_table = 'users'
  #   swappable = 'AUTH_USER_MODEL'