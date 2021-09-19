from django.db import models
from django.shortcuts import reverse
# Create your models here.


class ImportantDate(models.Model):
    date = models.DateTimeField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('formschapter:impdate-detail', args=[str(self.pk)])