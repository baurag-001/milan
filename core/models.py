from django.db import models

from ARrive.base_models import BaseModel


# Create your models here.
class Module(BaseModel):
    name = models.CharField(max_length=100)


class StudentGroup(BaseModel):
    name = models.CharField(
        max_length=100,
    )
