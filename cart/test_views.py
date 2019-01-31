from django.test import TestCase
from django.contrib.auth.models import User
from features.models import Feature
from django.core.urlresolvers import reverse
from django.test import Client
from .views import view_cart, add_to_cart, adjust_cart

class test_cart_views(TestCase):
    
    def test_view_cart_if_logged_in(self):
        '''test view_cart returns cart.html if logged in'''
        
        User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        page = client.get('/cart/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
        
        
    def test_view_cart_if_not_logged_in(self):
        '''test view_cart returns register_login.html if not logged in'''
        
        client = Client()
        page = client.get('/cart/', follow=True)
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register_login.html')
        
        
    def test_add_to_cart_route(self):
        ''' testing adding item to cart'''
        
        User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        response = client.post('/cart/add/{0}'.format(1), follow=True)
        
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,  b'{"msg": "all good here"}')
        
    