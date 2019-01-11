from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Feature(models.Model):
    
    
    feature_title = models.CharField(max_length=200, blank=False)
    feature_author = models.ForeignKey(User)
    details = models.TextField(blank=False)
    purchased = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False, blank=False)
    
    def __str__(self):
        return self.feature_title
        
        
class  PurchasedCount(models.Model):
    ''' count how many were purchased'''
    
    creator = models.ForeignKey(User)
    name = models.ForeignKey(Feature)
    
    
    class Meta:
       unique_together = ("creator", "name")
     
       
    def __str__(self):
        return str(self.creator)
