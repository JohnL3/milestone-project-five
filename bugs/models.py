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
    bugauthor = models.ForeignKey(User)
    bug_status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='O')
    upvotes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    initial_comment = models.TextField(blank=False)
    
    
    def __str__(self):
        return self.bug_title
        
        
class BugComment(models.Model):
    ''' Single bug comment'''
    
    AUTHOR_STATUS = (
            ('A', 'Admin'),
            ('S', 'Staff'),
            ('U', 'User')
        )
    
    bugid = models.ForeignKey(Bug)
    comment = models.TextField(blank=False)
    commentauthor = models.ForeignKey(User)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author_status = models.CharField(max_length=1, choices=AUTHOR_STATUS, default='U')
    
    def __str__(self):
        return str(self.commentauthor)
        

class  BugVotes(models.Model):
    ''' upvote bug'''
    
    voterid = models.ForeignKey(User)
    bugid = models.ForeignKey(Bug)
    
    
    class Meta:
       unique_together = ("voterid", "bugid")
     
       
    def __str__(self):
        return str(self.voterid)
       
    