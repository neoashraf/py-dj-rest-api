from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

    
class UserProfileManager(BaseUserManager):
    """Helps dgango work with our custom user model"""
    
    def create_user(self, email, name, password=None):
        """Creates new user profile object."""
    
        if not email:
            raise ValueError('User must have an email address.')
        
        email = self.normalize_email(email)
        user  = self.model(email= email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with the given details."""
        
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user
    
# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    
    """Represents a user profile in our system"""
    
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIREDC_FIELDS = ['name']
    
    def get_full_name(self):
        """Used to get full name of a user"""
        return self.name
    
    def get_short_name(self):
        """Used to get short name of a user"""    
        return self.name
    
    def __str___(self):
        """Django uses this when it needs to convert the object to a string"""    
        return self.email
    
