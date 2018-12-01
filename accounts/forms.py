from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    username.widget.attrs.update({'id': 'id_username_login', 'class': 'all-columns'})
    password.widget.attrs.update({'class': 'all-columns'})
    
    '''
    class Meta:
        model = User
        fields = ['username', 'password']
       
    def clean_username(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        print(username)
        print(password)
        if not User.objects.filter(username=username):
            print('fails username')
            raise forms.ValidationError(u'Your username or password is incorrect..')
        
        if User.objects.filter(password=password):
            print('fails password')
            raise forms.ValidationError(u'Your username or password is incorrect..')
        
        
        return username
    '''   
    
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    
    password1.widget.attrs.update({'class': 'all-columns'})
    password2.widget.attrs.update({'class': 'all-columns'})
    username.widget.attrs.update({'class': 'all-columns'})
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    '''
    def clean_email(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username):
            raise forms.ValidationError(u'username must be uniqueeeeeeeeeeeeeeeeeee')
        return username
    '''  
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username):
            raise forms.ValidationError(u'A user allready exists with this username..')
        return username
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError('Please confirm your password')
       
        if password1 != password2:
            raise forms.ValidationError('Passwords must match..')
           
        return password2
    