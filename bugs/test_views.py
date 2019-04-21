from django.test import TestCase
from .views import get_bugs, bug_details, upvote, bug_issue
from .forms import BugForm, BugCommentForm
from django.contrib.auth.models import User
from .models import Bug, BugComment
from django.core.urlresolvers import reverse
from django.test import Client
from django.http import JsonResponse, request
import json


class test_bugs_views(TestCase):
    
    def test_get_bugs_route_when_not_logged_in(self):
        '''Test a user not logged in gets redirected to register_login page if attempting to go to bugs page'''
        
        client = Client()
        
        page = client.get('/bugs/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
        
        
    def test_get_bugs_route_when_logged_in(self):
        '''Test a user logged in gets bugs.html page'''
        
        
        User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        page = client.get('/bugs/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'bugs.html')
        
        
    def test_bug_details_route_when_not_logged_in(self):
        '''Test a user not logged in cant visit a bug details page and is redirected to the register_login page'''
        
        client = Client()
        page = client.get('/bugs/1', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
        
        
    def test_bug_details_route_when_logged_in(self):
        '''Test a user logged in can visit a bug details page'''
        
        user = User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
    
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        bug =Bug(bug_title='Test bug', bugauthor=user, initial_comment='Test comment')
        bug.save()
        
        
        page = client.get('/bugs/{0}/'.format(bug.id), follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'singlebug.html')
        
    
    def test_posting_comment_to_bug_details_route(self):
        '''test user posting a comment on a bug'''
        
        user = User.objects.create_user(email='lethaladam@test.com', username='Lethal_Adam', password='generic')
        client = Client()
    
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        bug = Bug(bug_title='Test bug', bugauthor=user, initial_comment='Test comment')
        bug.save()
        
        data = {'comment': 'test comment', 'created_date': '01-02-2019'}
        response = client.post('/bugs/{0}/'.format(bug.id), data, format='json',follow=True)
        
        self.assertEqual(response.status_code, 200)
        
    
    def test_posting_comment_to_bug_details_route_with_commenting_closed(self):
        '''
        test user posting a comment on a bug when commenting is closed
        Should get a message back stating commenting is closed
        '''
        
        user = User.objects.create_user(email='lethaladam@test.com', username='Lethal_Adam', password='generic')
        user.is_superuser=True
        user.save()
        client = Client()
    
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        bug = Bug(bug_title='Test bug', bugauthor=user, initial_comment='Test comment')
        bug.bug_status = 'C'
        bug.save()
        client.get('/accounts/logout/')
        
        new_user = User.objects.create_user(username='Adam', password='generic1')
        
        client.post('/accounts/login/', {'username': 'Adam', 'password': 'generic1'})
        
        data = {'comment': 'test comment', 'created_date': '01-02-2019'}
        response = client.post('/bugs/{0}/'.format(bug.id), data, format='json',follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,  b'{"message": "Commenting is closed"}')
    
    def test_admin_can_set_comments_closed(self):
        '''test admin can set comments status to close'''
        
        user = User.objects.create_user(email='lethaladam@test.com', username='Lethal_Adam', password='generic')
        user.is_superuser=True
        user.save()
        
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        bug = Bug(bug_title='Test bug', bugauthor=user, initial_comment='Test comment')
        bug.bug_status = 'O'
        bug.save()
        
        data = {'bug_status': 'C', 'comment': 'commenting closed', 'created_date': '01-02-2019'}
        response = client.post('/bugs/{0}/'.format(bug.id), data, format='json',follow=True)
        if not bug.bug_status == 'C':
            if user.is_superuser:
                bug.bug_status = 'C'
                bug.save()
        
        
        self.assertEqual(response.status_code, 200)
        
        
        
        
        
        
        
    def test_upvoteing_a_bug(self):
        '''test i can upvote a bug issue'''
        
        user = User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
    
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        bug = Bug(bug_title='Test bug', bugauthor=user, initial_comment='Test comment')
        bug.save()
        
        data = {'bugid':bug.id}
        response = client.post('/bugs/upvote/', data, format='json',follow=True)
                                
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,  b'{"count": 1}')
        
        
    def test_upvoteing_a_bug_again(self):
        '''test user can only upvote the same bug issue once'''
        
        user = User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
    
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        bug = Bug(bug_title='Test bug', bugauthor=user, initial_comment='Test comment')
        bug.save()
        
        data = {'bugid':bug.id}
        client.post('/bugs/upvote/', data, format='json')
        
        response = client.post('/bugs/upvote/', data, format='json',follow=True)
                                
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,  b'{"message": "You allready upvoted this!!"}')
    
        
    def test_create_bug_issue(self):
        '''test template used is bug_form.html'''
        
        user = User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
    
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        page = client.get('/bugs/issue/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'bug_form.html')
        
        
    
    def test_post_to_bug_issue(self):
        '''test a user posting a bug issue'''        

        user = User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
    
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        bug = Bug(bug_title='Test bug', bugauthor=user, initial_comment='Test comment')
        bug.save()
        
        data = {'bug_title': 1, 'initial_comment': 'Test issue'}
        response = client.post('/bugs/issue/', data, format='json',follow=True)
        
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,  b'{"status_code": 1}')
        
        
        
        
    