from django.db import models


class Blog(models.Model):
    image = models.FileField(upload_to="blog_images/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    likes = models.IntegerField()
    reposts = models.IntegerField()
