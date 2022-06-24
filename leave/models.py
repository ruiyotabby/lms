from django.db import models
# Create your models here.
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, pjnumber, password=None):
        if not pjnumber:
            raise ValueError('Users must have pj numbers')
        user = self.model(
            pjnumber=pjnumber,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, pjnumber, password):
        user = self.create_user(
            pjnumber, passwword=password
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, pjnumber, password):
        user = self.create_user(
            pjnumber,
            password=password
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pjnumber = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50)
    designation = models.CharField(max_length=50)
    station = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    # name = fname + '' + lname

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
        """Does User have user specific permissions?"""#Yes, always
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    object = UserManager()

    """ 
    from django.contrib.auth import get_user_model
    user = get_user_model()
    """