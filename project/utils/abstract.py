from django.db import models
from django.utils import timezone


class DateTimeAbstractModel(models.Model):
    """ abstract class with created at and updated at fields """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
