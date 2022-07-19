from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.utils import timezone
# Create your models here.

class Link(models.Model):
    # DB Fields
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.created_date = timezone.now()
        self.slug = slugify(self.target_url)
        super().save(*args, **kwargs)
        pass

    def __str__(self):
        return self.target_url