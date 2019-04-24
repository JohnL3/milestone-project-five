from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile
from django.core.files.images import get_image_dimensions



class UserLoginForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    username.widget.attrs.update({'id': 'id_username_login', 'class': 'all-columns'})
    password.widget.attrs.update({'class': 'all-columns'})
    
      
    
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    
    email.widget.attrs.update({'autofocus': 'autofocus'})
    password1.widget.attrs.update({'class': 'all-columns'})
    password2.widget.attrs.update({'class': 'all-columns'})
    username.widget.attrs.update({'class': 'all-columns'})
    
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise forms.ValidationError(u'A user allready exists with this Email..')
        return email
       
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
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        
        if image:
            w, h = get_image_dimensions(image)
            if w <= 200 and h <= 200 and w == h:
                return image
            else:
                raise forms.ValidationError("The image should be square with width and height less or equal to 200")
        else:
            raise forms.ValidationError("No image found")
        return image
    
