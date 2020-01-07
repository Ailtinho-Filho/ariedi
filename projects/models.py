from django.db import models

from category.models import Category


class Project(models.Model):
    category = models.ManyToManyField(Category)
    score = models.PositiveIntegerField(blank=True, null=True, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)
    link = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['score']

    def __str__(self):
        return self.title
