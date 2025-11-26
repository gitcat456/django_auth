from django.db import models
from django.contrib.auth.models import AbstractUser  


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    date_joined = models.DateTimeField()
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
        ('rider', 'Rider'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='vendor')
    
    def is_admin(self):
        return self.role == 'admin'
    def is_vendor(self):
        return self.role == 'vendor'
    def is_vendor(self):
        return self.role == 'rider'
