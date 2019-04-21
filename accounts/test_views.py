from django.test import TestCase
from .views import index, login, register, register_login, logout
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client


class Test_accounts_views(TestCase):
    
    def test_index(self):
        '''Test get sent to index page'''
        
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
        
        
    def test_logout_if_user_logged_in(self):
        '''Test to make sure if user logged in and clicks logout he gets logged out and redirected to index page'''
        
        User.objects.create_user(username='Ems_1', password='generic')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic'})
        
        
        response = client.get('/accounts/logout/', follow=True)
    
        self.assertRedirects(response, expected_url=reverse('index'), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
    def test_register_login(self):
        '''Test user can go to register_login page if not logged in'''
        
        page = self.client.get('/accounts/register_login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
        
    
    def test_register_login_if_allready_logged_in(self):
        '''Test user is redirected to index page if trying to access register_login page when allready logged in'''
        
        User.objects.create_user(username='Ems_1', password='generic')
        client = Client()
       
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic'})
        
        client.get('/accounts/register_login/', follow=True)
        
        response = client.get(reverse('register_login'))
        
        self.assertRedirects(response, expected_url=reverse('index'), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
    def test_login(self):
        '''Test if user trys to use GET the accounts/login they will be redirected to register_login page if not logged in'''
        
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
    
    def test_post_login_with_proper_login_details(self):
        '''Test user can login using proper details and gets redirected to index page on successful login'''
        User.objects.create_user(username='Ems_1', password='generic')
        client = Client()
        
        page = client.post('/accounts/login/', {'username':'Ems_1', 'password': 'generic'}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
        
    
    def test_post_login_with_wrong_login_details(self):
        '''Test login fails and redirects to register_login if login details are incorrect'''
        
        User.objects.create_user(username='Ems_1', password='generic')
        client = Client()
        
        wrong_password = {
            'username': 'testuser',
            'password': 'secret1'
        }
        
        page = client.post('/accounts/login/', wrong_password, follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
        
        
    def test_login_user_logged_in_allready(self):
        '''
        Test if user is logged in they get redirected to index page
        
        https://stackoverflow.com/questions/27985598/how-to-test-django-redirect-from-view-class
        '''
        User.objects.create_user(username='Ems_1', password='generic')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic'}, follow=True)
        
        response = client.get(reverse('login'))
        
        self.assertRedirects(response, expected_url=reverse('index'), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
    
        
    def test_GET_register_if_not_logged_in(self):
        '''Test if user trys to use GET the accounts/register they will be redirected to register_login page if not logged in'''
        
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
        
            
    def test_register_if_logged_in(self):
        '''Test if user trys to use GET the accounts/login they will be redirected to index page if logged in'''
        
        User.objects.create_user(username='Ems_1', password='generic')
        client = Client()
                                    
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic'})
        
        response = client.get('/accounts/register/', follow=True)
        
        self.assertRedirects(response, expected_url=reverse('index'), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
    def test_valid_register_form(self):
        '''test with valid form post to register route you get redirected to index route'''
        
        client = Client()
        response = client.post(reverse('register'),{'email': 'emily@test.com','username': 'Ems_1','password1': 'generic','password2': 'generic'})
                                          
        self.assertRedirects(response, expected_url=reverse('index'), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
    
        
        
          
        
        
        
        

