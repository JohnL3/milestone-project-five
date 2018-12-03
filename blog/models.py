from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''A single blog post'''
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date =models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __unicode__(self):
        return self.title
