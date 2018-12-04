from django.test import TestCase
from .views import get_posts, single_post, create_edit_post
from django.contrib.auth.models import User
from .models import Post
from django.core.urlresolvers import reverse
from django.test import Client

class Test_blog_views(TestCase):
    
    
    def test_get_post_route(self):
        '''Test to ensure the blogposts.html is used'''
        
        page = self.client.get('/blog/posts/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blogposts.html')
        
    
    def test_single_post_route(self):
        '''Test to ensure the singlepost.html is used'''
        
        post = Post(title='test post')
        post.save()
        print(post.id)
        
        page = self.client.get('/blog/posts/{0}/'.format(post.id))
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'singlepost.html')
        
    
    def test_access_create_edit_post_when_not_logged_in(self):
        ''' test to ensure blogposts.html is used if user not logged in when trying to access blog/posts/new '''

        page = self.client.get('/blog/posts/new/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blogposts.html')
        
        
    def test_access_create_edit_post_logged_in_as_normal_user(self):
        '''Test ordinary logged in user trying to get to blog/posts/new route'''
        
        User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        page = client.get('/blog/posts/new/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blogposts.html')
        
        
    def test_access_create_edit_post_logged_in_as_staff_user(self):
        '''Test user.is_staff logged in trying to get to blog/posts/new should get blogform.html'''
        
        user = User.objects.create_user(username='Ems_1', password='generic1')
        user.is_staff=True
        user.save()
        
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic1'})
        
        page = client.get('/blog/posts/new/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blogform.html')
        
        
    def test_POST_access_create_edit_post_logged_in_as_staff_user(self):
        '''Test user.is_staff logged in trying to POST to blog/posts/new should get blogform.html'''
        
        user = User.objects.create_user(username='Ems_1', password='generic1')
        user.is_staff=True
        user.save()
        
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic1'})
        
        
        page = client.post('/blog/posts/new/',{'title': 'test'}, follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blogform.html')
        
    
    def test_POST_access_create_edit_post_logged_in_as_super_user(self):
        '''Test user.is_superuser logged in trying to POST to blog/posts/new should get single_post.html'''
        
        user = User.objects.create_user(username='JohnL3', password='test1')
        user.is_superuser=True
        user.save()
        
        client = Client()
        
        client.post('/accounts/login/', {'username': 'JohnL3', 'password': 'test1'})
        
        
        page = client.post('/blog/posts/new/',{'title': 'test', 'content': 'hello'}, follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'singlepost.html')
    
    
        
        
    