from django.db import models

# Create your models here.
class BlogPost(models.Model):
    #user
    blog_id = models.AutoField(primary_key=True)
    judul_blog = models.CharField(max_length=100)
    blog_text = models.TextField()
    post_time = models.DateTimeField(blank=True, null=True)