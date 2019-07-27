from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin



# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile in our system"""
    
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = modelBooleanField(default=True)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIREDC_FIELDS = ['name']
    
    def get_full_name(self):
        """Used to get full name of a user"""
        return self.name
    
    def get_short_name(self)
        """Used to get short name of a user"""    
        return self.name
    
    def __str___(self)
        """Django uses this when it needs to convert the object to a string"""    
        return self.email