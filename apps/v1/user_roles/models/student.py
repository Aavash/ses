from django.conf import settings
from django.db import models

from apps.v1.commons.models import CreatedModified


class Student(CreatedModified):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    school = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email
