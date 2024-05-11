from django.db import models  # Create your models here.


class BlogLink(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title
