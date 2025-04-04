# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
# from django.db import models
# from django.utils import timezone


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     USER_ROLE = [
#         ('1', 'Customer'),
#         ('2', 'Editor'),
#         ('3', 'Vendor'),
#     ]
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     mobile = models.PositiveIntegerField()
#     user_role = models.CharField(choices=USER_ROLE, default=1, max_length=20)
#     date_joined = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)


#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name','mobile']

#     def __str__(self):
#         return self.email


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.utils import timezone

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     USER_ROLE = [
#         ('1', 'Customer'),
#         ('2', 'Editor'),
#         ('3', 'Vendor'),
#     ]
    
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     mobile = models.PositiveIntegerField()
#     user_role = models.CharField(choices=USER_ROLE, default='1', max_length=20)
    
#     # Vendor specific fields
#     trade_license_number = models.CharField(max_length=100, null=True, blank=True)
#     gst_number = models.CharField(max_length=15, null=True, blank=True)
    
#     date_joined = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

#     def __str__(self):
#         return self.email

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_ROLE = [
        ('1', 'Customer'),
        ('2', 'Editor'),
        ('3', 'Vendor'),
    ]
    
    # Common fields
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.PositiveIntegerField()
    user_role = models.CharField(choices=USER_ROLE, default='1', max_length=20)
    
    # Vendor specific fields
    trade_license_number = models.CharField(max_length=100, null=True, blank=True)
    gst_number = models.CharField(max_length=15, null=True, blank=True)
    
    # New fields for image and customer type
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    customer_type = models.CharField(
        choices=[('Personal', 'Personal'), ('Corporate', 'Corporate')],
        default='Personal',
        max_length=20
    )
    
    # Meta fields
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    # Custom user manager
    objects = CustomUserManager()

    # Required fields for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    def __str__(self):
        return self.email
