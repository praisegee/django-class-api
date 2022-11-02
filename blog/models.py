from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    @property
    def url_path(self):
        try:
            url = self.img.url
        except ValueError:
            url = ""

        return url
