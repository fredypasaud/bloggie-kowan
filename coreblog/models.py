from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    judul_blog = models.CharField(max_length=100)
    blog_text = models.TextField()
    post_time = models.DateTimeField(blank=True, null=True)