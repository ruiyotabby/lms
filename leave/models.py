from django.db import models
# Create your models here.
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class User(AbstractBaseUser):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pjnumber = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50)
    designation = models.CharField(max_length=50)
    station = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    name = fname + '' + lname

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) #admin user
    admin = models.BooleanField(default=False)#super user

    USERNAME_FIELD = 'pjnumber'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        #user is identified by name
        return self.name
    
    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does User have user specific permissions?"#Yes, always
        return True

    def has_module_perm(self, perm, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin