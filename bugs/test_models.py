from django.test import TestCase
from .models import Bug, BugComment, BugVotes
from django.utils import timezone
from django.contrib.auth.models import User

class TestBugModel(TestCase):
    '''Test i can create a bug'''
    
    def test_can_create_a_bug(self):
        '''create a bug'''
         
        user = User.objects.create_user(username='Ems_1', password='generic')
        bug=Bug(bug_title='Test title', bugauthor=user, initial_comment='A test comment')
        bug.save()
         
        self.assertEqual(bug.bug_title, 'Test title')
        self.assertEqual(bug.bugauthor, user)
        self.assertEqual(bug.bug_status, 'O')
        self.assertEqual(bug.upvotes, 0)
        self.assertEqual(bug.initial_comment, 'A test comment')
        self.assertEqual(bug.__str__(), bug.bug_title)
        
        
class TestBugCommentModel(TestCase):
    '''Test i can create a bug comment'''
    
    def test_can_create_bug_comment(self):
        '''create a single bug comment'''
        
        user = User.objects.create_user(username='Ems_1', password='generic')
        bug=Bug(bug_title='Test title', bugauthor=user, initial_comment='A test comment')
        
        comment = BugComment(bugid=bug, comment='Single test comment', commentauthor=user)
        
        self.assertEqual(comment.bugid, bug)
        self.assertEqual(comment.commentauthor, user)
        self.assertEqual(comment.__str__(), str(comment.commentauthor))
        
        
class TestBugVotesModel(TestCase):
    '''Test BugVotes model'''
    
    def test_can_vote(self):
        '''test i can vote up a bug issue'''
        
        user = User.objects.create_user(username='Ems_1', password='generic')
        bug=Bug(bug_title='Test title', bugauthor=user, initial_comment='A test comment')
        
        upvote = BugVotes(voterid=user, bugid=bug)
        
        self.assertEqual(upvote.voterid, user)
        self.assertEqual(upvote.bugid, bug)
        self.assertEqual(upvote.__str__(), str(upvote.voterid))
        
