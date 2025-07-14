from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomerUser(AbstractUser):
    username = None 
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/',blank = True, null=True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []  # no other required fields
    # Add more fields and user profile image
    # only allow .png, .jpeg, .jpg and max 3 MB imnage size

    objects = CustomUserManager()

    def __str__(self):
        return self.email
