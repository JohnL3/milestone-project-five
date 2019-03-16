from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
import json
from django.utils import timezone
from .models import Bug, BugComment, BugVotes
from .forms import BugCommentForm, BugForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def get_bugs(request):
    '''Get a list of all bugs and render them'''
    
    bugs = Bug.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    
    return render(request,'bugs.html', {'bugs': bugs})


@login_required
def bug_details(request, pk):
    '''Get and post to a singel bug detail'''
    
    if request.method == 'POST':
        
        # get bug object 
        bug = Bug.objects.get(pk=pk)
        
        # if bug_status not closed proceed eles return message stateing commenting is close
        # doing a check here in case anyone tries to get around my disableing comment section on frontend
        if not bug.bug_status == 'C':
        
            if request.user.is_superuser:
                
                # superuser can change the status of bug from open to doing to closed
                bug_status = request.POST.get('bug_status')
                
                #update bug status if it has changed
                if not bug_status == bug.bug_status:
                    bug.bug_status = bug_status
                    bug.save()
                
                
            # get the users comment about the bug
            comment_text = request.POST.get('comment')
           
            # wont accept date format so cant add it to model
            created_date = request.POST.get('created_date')
           
            
            # save comment to the database
            comment = BugComment(bugid_id = pk, comment=comment_text, commentauthor_id = request.user.id)
            comment.save()
            
        
            response_data = {}
            
            response_data['comment_text'] = comment_text
            response_data['bug_id'] = pk
            response_data['user_id'] = request.user.id
            response_data['created_date'] = created_date
            response_data['username'] = request.user.username
            response_data['avatar_url'] = request.user.profile.avatar_url
            response_data['bug_status']= bug.get_bug_status_display()
            
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            response_data = {}
            response_data['message'] = 'Commenting is closed'
            
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
        # get a bug by an id 
        bug = get_object_or_404(Bug, pk=pk)
        
        bug_status = bug.get_bug_status_display()
        
        # get all comments associated with bug
        comments = BugComment.objects.filter(bugid=pk).order_by('created_date')
        
        ''' Send a form down for users to add comments on bug issue'''
        form = BugCommentForm()
        
        context ={
            'bug': bug,
            'user_id': request.user.id,
            'form': form,
            'comments': comments,
            'bug_status': bug_status,
            'avatar_url': request.user.profile.avatar_url
        }
           
        return render(request, 'singlebug.html', context)
   
    
@login_required   
def upvote(request):
    '''Upvote a bug'''
    
    if request.method == 'POST':
    
        response_data = {}
        
        voterid = request.user.id
        bugid = request.POST.get('bugid')
        
        # get the bug object by id
        upvotes = Bug.objects.get(pk=bugid)
        
        # check if the bugid voterid combination has allready being used
        upvote = BugVotes.objects.filter(bugid=bugid, voterid=voterid)
        
        #if combination has not being used allow to vote else return
        if not upvote:
            
            # save the vote to databaase
            upvote = BugVotes(bugid_id = bugid, voterid_id = request.user.id)
            upvote.save()
            
            #count votes for specific bug by id
            count = BugVotes.objects.filter(bugid_id=bugid).count()
            
            # update upvotes field in specific bug
            upvotes.upvotes = count
            upvotes.save()
            
            
            response_data['count'] = count
    
            return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )
            
        else:
            response_data = {}
            response_data['message'] = 'You allready upvoted this!!'
    
            return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )


@login_required
def bug_issue(request, pk=None):
    ''' Add new issue to database or get bug form'''
    
    if request.method == 'POST':
        #get instance of bug object
        bug = Bug()
       
        bug_title = request.POST.get('bug_title')
        initial_comment =request.POST.get('initial_comment')
        
        #get the author id
        author_id = request.user.id
        
        # fill in the details and save
        bug.bug_title=bug_title 
        bug.bugauthor_id=author_id
        bug.initial_comment=initial_comment
        bug.bug_author_avatar=request.user.profile.avatar_url
        bug.save()
        
        response = {'status_code': 1} 
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        #get form and send with html
        form = BugForm()
        return render(request, 'bug_form.html',{'form': form})