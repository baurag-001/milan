import uuid

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models

from ARrive.base_models import BaseModel
from core.models import StudentGroup, Module


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('normal_user', 'Normal User'),
        ("superuser", "Superuser"),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    )
    email = models.EmailField(
        _('email address'),
    )
    first_name = models.CharField(
        max_length=200,
        null=True,
    )
    last_name = models.CharField(
        max_length=200,
        null=True,
    )

    user_type = models.CharField(
        choices=USER_TYPE_CHOICES,
        max_length=14,
        default='normal_user'
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_temporary = models.BooleanField(
        _('temporary'),
        default=False,
        help_text=_(
            'Designates whether this user is temporary i.e not signed up but made by system itself'
        ),
    )
    is_archived = models.BooleanField(default=False)
    # Define related names for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='users',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.username if self.username else self.email

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Student(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    student_group = models.ForeignKey(
        StudentGroup,
        on_delete=models.CASCADE
    )


class Teacher(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE
    )
