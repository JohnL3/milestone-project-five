from django.test import TestCase
from .views import get_features, single_feature, feature_form
from django.contrib.auth.models import User
from .models import Feature
from django.core.urlresolvers import reverse
from django.test import Client


class test_feature_views(TestCase):
    
    def test_get_features_if_not_logged_in(self):
        '''test to make sure user not logged in trying to go to get_features route is sent to register_login'''
        
        client = Client()
        
        page = client.get('/features/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
        
        
    def test_get_features_if_logged_in(self):
        '''test to ensure features.html is returned if user is logged in and visits get_features'''
        
        user = User.objects.create_user(username='Ems_1', password='generic1')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic1'})
        
        page = client.get('/features/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'features.html')
        
        
    def test_single_feature_route(self):
        
        user = User.objects.create_user(username='Ems_1', password='generic1')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic1'})
        feature=Feature(feature_title='Test', feature_author=user, details='New feature',price=50.00, paid=False)
        feature.save()
        
        
        page = client.post('/features/1/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'singlefeature.html')
        
        
    def test_feature_form_route_get(self):
        '''test if logged in user goes to route featureform.html is used'''
        
        user = User.objects.create_user(username='Ems_1', password='generic1')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic1'})
        
        page = client.get('/features/details/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'featureform.html')
        
        
    def test_feature_form_route_post(self):
        '''test if logged in user posts to route singlefeature.html is used'''
        
        user = User.objects.create_user(username='Ems_1', password='generic1')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Ems_1', 'password': 'generic1'})
        
        page = client.post('/features/details/', {'feature_title':'Test Feature', 'details': 'A test feature'}, follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'singlefeature.html')
        
       
        