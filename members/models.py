from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from try_django import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class MemberProfileManager(BaseUserManager):
    """Manager for member profiles"""

    def create_user(self, username, first_name, last_name, password=None):
        """Create a new user profile"""
        if not username:
            raise ValueError('User must have an email address')

        if not first_name:
            raise ValueError('Please provide your first name')

        if not last_name:
            raise ValueError('Please provide your last name')

        username = self.normalize_email(username)
        user = self.model(username=username, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, first_name, last_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(username, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user


class MemberProfile(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(max_length=200)
    join_date = models.DateTimeField(default=timezone.now, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    objects = MemberProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        fullname = self.first_name+'_'+ self.last_name
        """Retrieve full name of user"""
        return fullname

    def get_username(self):
        return self.username

    def get_email(self):
        return self.username

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.first_name

    def __str__(self):
        """Return string representation of our user"""
        return self.username

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

account_activation_token = TokenGenerator()