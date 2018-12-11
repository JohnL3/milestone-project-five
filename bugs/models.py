from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bug(models.Model):
    '''single bug'''
    
    STATUS_CHOICE = (
            ('O', 'Open'),
            ('D', 'Doing'),
            ('C', 'Closed')
        )
        
    bug_title = models.CharField(max_length=200, blank=False)
    bug_author = models.ForeignKey(User, default=None)
    bug_status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='O')
    upvotes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    initial_comment = models.TextField(blank=False)
    
    
    def __str__(self):
        return self.bug_title
        
        
class BugComment(models.Model):
    ''' Single bug comment'''
    
    comment = models.TextField(blank=False)
    comment_author = models.ForeignKey(User, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.comment_author)
        

class  BugVotes(models.Model):
    ''' upvote bug'''
    
    voter_id = models.ForeignKey(User, default=None)
    bug_id = models.ForeignKey(Bug, default=None)
    
    
    class Meta:
       unique_together = ("voter_id", "bug_id")
     
       
    def __str__(self):
        return self.user
       
    