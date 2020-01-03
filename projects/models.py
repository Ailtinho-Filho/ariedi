from django.db import models


class Project(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)
    link = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
