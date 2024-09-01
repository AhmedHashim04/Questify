from django.db import models

class Info(models.Model):
    place = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self) -> str:
        return self.email