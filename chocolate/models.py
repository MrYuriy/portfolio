from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    home_link = models.CharField(max_length=200)
    short_description = models.TextField()
    long_deskription = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name