from django.db import models

from category.models import Category


class Workshop(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "workshops"

    def __str__(self):
        return self.title


def get_image_filename(instance, filename):
    image_id = instance.workshop.id
    return f"workshop_images/{image_id}"


class WorkshopImage(models.Model):
    workshop = models.ForeignKey(Workshop, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')
