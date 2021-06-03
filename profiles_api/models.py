from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser  # Added : Default user models
from django.contrib.auth.models import PermissionsMixin  # Added : Default user models
from django.contrib.auth.models import BaseUserManager   # Added : Default user models


class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, name, passowrd=None):
        """" Create a new user profile"""
        if not email:
            raise ValueError("User must have a email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(passowrd)  # Encryp the password 
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, passowrd):
        """ cREATE AND SAVE A NEW SUPER USER WITH GIVEN DETAILS """
        user = self.create_user(email, name, passowrd)

        user.is_superuser = True
        user.is_staff =  True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database MOdel for users in the systema """
    email = models.EmailField(max_length=255, unique=True)
    name =  models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """ Retrieve full name of the user """
        return self.name

    def get_short_name(self):
        """ Retrieve short name of the user """
        return self.name

    def __str__(self):
        """ Return strign representation of pur user """
        return self.email