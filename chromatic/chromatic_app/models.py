from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField(null=False, blank=False)
    annotatedImage = models.ImageField(null=True, blank=True)
    uploader = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    caption = models.CharField(max_length=400, null=False, blank=False)
    public = models.BooleanField(default=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

class Face(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    topLeftX = models.IntegerField(null=False)
    topLeftY = models.IntegerField(null=False)
    width = models.IntegerField(null=False)
    height = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.post.pk}-({self.topLeftX}, {self.topLeftY})'