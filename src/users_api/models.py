from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

MESSAGE_NO_EMAIL = "Please fill an email adress !"
MESSAGE_NO_PSEUDO = "Please fill a pseudo !"
MESSAGE_NO_ADMIN = "This role is not allowed !"
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, pseudo, first_name, last_name, email, role, password=None):
        if not pseudo:
            raise ValueError(MESSAGE_NO_PSEUDO)

        if not email:
            raise ValueError(MESSAGE_NO_EMAIL)

        user = self.model(
            pseudo=pseudo,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            role=role,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, pseudo, first_name, last_name, email, role, password=None):
        user = self.create_user(pseudo=pseudo, first_name=first_name,
                                last_name=last_name,
                                email=email,
                                role=role,
                                password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class UserProfile(AbstractBaseUser):
    ROLES = (
        ('COM', 'Commercial'),
        ('SUP', 'Support'),
        ('GES', 'Gestion')
    )
    pseudo = models.CharField(unique=True, max_length=10, blank=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, max_length=100, blank=False)
    role = models.CharField(max_length=55, choices=ROLES, verbose_name="Type de rôle")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "pseudo"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "role"]
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        if self.is_admin is True:
            self.role = "GES"
        super(UserProfile, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
