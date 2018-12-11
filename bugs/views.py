from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Bug, BugComment, BugVotes

from django.contrib.auth.decorators import login_required



def get_bugs(request):
    '''Get a list of all bugs and render them'''
    
    bugs = Bug.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    
    return render(request,'bugs.html', {'bugs': bugs})


def bug_details(request, pk):
    '''Create a view that returns a single bug details'''
    bug = get_object_or_404(Bug, pk=pk)
    comments = BugComment.objects.filter(BugComment_id=pk)
    print('id', pk)
    print('author',bug.bug_author)
    
    return render(request, 'singlebug.html', {'bug': bug}, {'comments': comments})