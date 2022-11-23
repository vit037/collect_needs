from django.conf import settings
from django.db import models
from django.utils import timezone

class Instite(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    inn = models.CharField(max_length=12)
    kpp = models.CharField(max_length=12)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title