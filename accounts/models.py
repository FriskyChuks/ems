from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, Group
)

GENDER = (
		('male', 'Male'),
		('female', 'Female'),
	)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None, is_staff=False, is_admin=False, is_active=True):
        if not first_name:
            raise ValueError("User must have firstname!")
        if not last_name:
            raise ValueError("User must have lastname!")
        if not email:
            raise ValueError("User must have an email!")
        if not password:
            raise ValueError("Users must have password!")

        user_obj = self.model(
            # username = username,
            email =self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        # user_obj.is_a_patient = is_patient
        user_obj.save(using=self._db)
        return user_obj


    def create_staff(self, email, first_name=None, last_name=None, password=None):
        user = self.create_user(
            # username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True
        )
        return user


    def create_superuser(self, email, first_name=None, last_name=None, password=None):
        user = self.create_user(
            # username,
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    foto			= models.ImageField(null=True, blank=True, upload_to="image/", default="image/male.jpg")
    email 			= models.EmailField(max_length=255, unique=True)
    first_name		= models.CharField(max_length=225)
    last_name		= models.CharField(max_length=225)
    other_names		= models.CharField(max_length=225, blank=True, null=True)
    phone1          = models.CharField(max_length=11,null=True,blank=True)
    phone2          = models.CharField(max_length=11, blank=True, null=True)
    gender          = models.CharField(null=True, blank=True,max_length=10, choices=GENDER)
    active 			= models.BooleanField(default=False)
    staff 			= models.BooleanField(default=False)
    is_shop_owner 	= models.BooleanField(default=False)
    is_resident 	= models.BooleanField(default=False)
    admin			= models.BooleanField(default=False)
    group 			= models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    timestamp 		= models.DateTimeField(auto_now_add=True, auto_now=False)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ["first_name","last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return str(self.first_name) + " " + str(self.last_name)
    
    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def shop_owner(self):
        return self.is_shop_owner
    
    @property
    def resident(self):
        return self.is_resident