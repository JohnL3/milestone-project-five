from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
import json
from bugs.models import Bug
from features.models import Feature


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect(reverse('index'))
    
def index(request):
    return render(request, 'index.html')

def register_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    registration_form = UserRegistrationForm()
    login_form = UserLoginForm()
    return render(request, 'register_login.html', {'registration_form': registration_form, 'login_form': login_form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        registration_form = UserRegistrationForm()
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
                                    
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in.')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password is incorrect..')
                
    else:
        login_form = UserLoginForm()
    
    registration_form = UserRegistrationForm()
    return render(request, 'register_login.html', {'registration_form': registration_form, 'login_form': login_form})
    
    
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == 'POST':
        login_form = UserLoginForm()
        
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
        
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'] )
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Unable to register your account at this time.')
                
        
    else:
        registration_form = UserRegistrationForm()
    
    login_form= UserLoginForm 
    return render(request, 'register_login.html', {'registration_form': registration_form, 'login_form': login_form})


@login_required  
def profile(request):
    
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
       
        form = ProfileForm(request.POST, request.FILES)
        
        avatar_url ='images/'+str(request.FILES['file'])
        image = request.FILES['file']
        
        if form.is_valid():
            user.profile.avatar_url = avatar_url
            user.profile.image = image
            user.profile.save()
            
            avatar_url = user.profile.avatar_url
            
        return JsonResponse({'error': False, 'avatar_url': avatar_url})
    else:
        
        user = request.user
        avatar = request.user.profile.avatar_url
        profile_form = ProfileForm()
        
        my_issues = Bug.objects.filter(bugauthor=request.user.id)
        features = Feature.objects.filter(feature_author=request.user.id)
        show_button = Feature.objects.filter(paid=False, feature_author=user)
        
        return render(request, 'profile.html',
        {'user': user, 
        'avatar': avatar, 
        'profile_form': profile_form,
        'my_issues': my_issues,
        'features': features,
        'show_button': show_button
        })