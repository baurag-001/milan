import uuid

from django.db import models

from ARrive.base_models import BaseModel
from core.models import StudentGroup
from user.models import Teacher, Student


# Create your models here.
class ClassSchedule(BaseModel):
    CLASS_TYPE_CHOICES = (
        ('lecture', 'Lecture'),
        ('tutorial', 'Tutorial'),
        ('lab', 'Lab')
    )
    class_type = models.CharField(
        choices=CLASS_TYPE_CHOICES,
        default='lecture',
        max_length=30,
    )

    group = models.ForeignKey(
        StudentGroup,
        on_delete=models.CASCADE,
    )
    teacher = models.ManyToManyField(
        Teacher,
        blank=True,
    )


class Feedback(BaseModel):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
    )
    message = models.TextField()
