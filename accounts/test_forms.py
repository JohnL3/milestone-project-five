from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import Client

class Test_accounts_form(TestCase):
    '''Tests to check login form works'''
    
    def test_UserLoginForm_takes_username_and_password(self):
        '''Test to check form requires a username and a password'''
        
        form = UserLoginForm({'username': 'create test', 'password': 'generic'})
        self.assertTrue(form.is_valid())
        
       
    def test_UserRegistrationForm_fails_if_username_allready_exists(self):
        '''Test to check form is not valid if username is not unique'''
        
        self.user = User.objects.create(username="Ems_1", password="generic")
        
        form = UserRegistrationForm({'username': 'Ems_1', 'password1': 'generic', 'password2': 'generic'})
        self.assertFalse(form.is_valid())
        
    
    def test_UserRegistrationForm_is_not_valid_if_passwords_fields_are_different(self):
        '''Test to check form is not valid if password fields are different'''
    
        form = UserRegistrationForm({'username': 'create test', 'password1': 'generic', 'password2': 'genericOne'})
        self.assertFalse(form.is_valid())
        
        
    def test_UserRegistrationForm_is_not_valid_if_first_password_field_not_filled_in(self):
        '''Test to check form is not valid if password1 is not filled'''
         
        form = UserRegistrationForm({'username': 'Ems_1','password2':'generic'})
        self.assertFalse(form.is_valid())
        
    
   
        
    
        
        
        
    
        
        
        
        
        