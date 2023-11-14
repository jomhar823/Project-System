from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, user_type=None, barangay=None,  **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, barangay=barangay, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, user_type=None, barangay=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, user_type, barangay **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)  
    barangay = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=8, choices=(('mdrrmc', 'MDRRMC Admin'), ('barangay', 'Barangay Admin')), default='mdrrmc')
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

class Report(models.Model):
    SUBJECT_CHOICES = (
        ('Situational Report', 'Situational Report'),
        ('Incident Report', 'Incident Report'),
        # ('Flood Report', 'Flood Report'),
        # ('Earthquake Report', 'Earthquake Report'),
        # ('Landslide Report', 'Landslide Report'),
        # ('Weather Report', 'Weather Report'),
        # ('Typhoon Report', 'Typhoon Report'),
    )

    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='report_attachments/', blank=True, null=True)
    respondent_name = models.CharField(max_length=255)
    barangay = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    date_reported = models.DateField()
    time_reported = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class Announcement(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(null=True, blank=True)  
    barangay = models.ManyToManyField(CustomUser, related_name='announcements')

    def __str__(self):
        return self.subject

class AdminReport(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    origin = models.CharField(max_length=50)


class AdminNaturalReport(models.Model):
    SUBJECT_CHOICES = (
        ('Flood Report', 'Flood Report'),
        ('Earthquake Report', 'Earthquake Report'),
        ('Landslide Report', 'Landslide Report'),
        ('Weather Report', 'Weather Report'),
        ('Typhoon Report', 'Typhoon Report'),
    )

    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='report_attachments/', blank=True, null=True)
    date_reported = models.DateField()
    time_reported = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
