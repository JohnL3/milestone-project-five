from django.test import TestCase
from .views import checkout
from .forms import MakePaymentForm, OrderForm
from django.contrib.auth.models import User
from .models import Order, OrderLineItem
from django.core.urlresolvers import reverse
from django.test import Client
from django.http import JsonResponse, request
from features.models import Feature
import json


class checkout_views(TestCase):
    
    def test_get_checkout(self):
        '''test checkout uses checkout.html'''
        
        User.objects.create_user(username='Lethal_Adam', password='generic')
        client = Client()
        
        client.post('/accounts/login/', {'username': 'Lethal_Adam', 'password': 'generic'})
        
        response = client.get('/checkout/', follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
        
