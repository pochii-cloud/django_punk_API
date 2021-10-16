from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Favourites'
