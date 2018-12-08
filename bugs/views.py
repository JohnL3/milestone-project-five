from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone


from django.contrib.auth.decorators import login_required



def get_bugs(request):
    '''Get a list of all bugs and render them'''
    
    return render(request,'bugs.html')


def bug_details(request, pk):
    '''Create a view that returns a single bug details'''
    
    return render(request, 'singlebug.html')