from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
import json
from django.utils import timezone
from .models import Bug, BugComment, BugVotes
from .forms import BugCommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def get_bugs(request):
    '''Get a list of all bugs and render them'''
    
    bugs = Bug.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    
    return render(request,'bugs.html', {'bugs': bugs})


@login_required
def bug_details(request, pk):
    '''Create a view that returns a single bug details'''
    
    if request.method == 'POST':
        
        # get the users comment about the bug
        comment_text = request.POST.get('comment')
       
        # have to get a instance of foregin key
        bug = Bug.objects.get(id = pk)
        
        # have to get instance of foregin key
        user = User.objects.get(id = request.user.id)
        
        # wont accept date format so cant add it to model
        created_date = request.POST.get('created_date')
        
        if request.user.is_superuser:
            user_status = 'A'
        elif request.user.is_staff:
            user_status = 'S'
        else:
            user_status = 'U'
        
        # save comment to the database
        comment = BugComment(bug_id = bug, comment=comment_text, comment_author = user, author_status = user_status)
        comment.save()
        
        
        username = request.user.username
        
            
        response_data = {}
        
        response_data['comment_text'] = comment_text
        response_data['bug_id'] = pk
        response_data['user_id'] = request.user.id
        response_data['created_date'] = created_date
        response_data['username'] = username
        response_data['user_type'] = user_status
        
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        
        # get a bug by an id 
        bug = get_object_or_404(Bug, pk=pk)
        
        
        bug_status = bug.get_bug_status_display()
        
        # get all comments associated with bug
        comments = BugComment.objects.filter(bug_id=pk)
        
        ''' Send a form down for users to add comments on bug issue'''
        form = BugCommentForm()
        
        context ={
            'bug': bug,
            'user_id': request.user.id,
            'form': form,
            'comments': comments,
            'bug_status': bug_status
        }
           
        return render(request, 'singlebug.html', context)
    
    
