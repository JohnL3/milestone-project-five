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
        
        # checking if comment status is closed
        bug = Bug.objects.get(pk=pk)
        
        print(bug.bug_status)
        # if status not closed proceed eles return message stateing commenting is close
        # doing a check here in case anyone tries to get around my disableing comment section on frontend
        if not bug.bug_status == 'C':
        
            if request.user.is_superuser:
                # superuser can change the status of bug from open to doing to closed
                bug_status = request.POST.get('bug_status')
                #Bug.objects.filter(id = pk).update(bug_status=bug_status)
                if not bug_status == bug.bug_status:
                    bug.bug_status = bug_status
                    bug.save()
                
                
            # get the users comment about the bug
            comment_text = request.POST.get('comment')
           
            # have to get a instance of foregin key
            #bug = Bug.objects.get(id = pk)
            
            # have to get instance of foregin key
            #user = User.objects.get(id=request.user.id)
            #print('USER',user)
            
            # wont accept date format so cant add it to model
            created_date = request.POST.get('created_date')
            
            # setting status so I can display appropriate avatar with comment
            if request.user.is_superuser:
                user_status = 'A'
            elif request.user.is_staff:
                user_status = 'S'
            else:
                user_status = 'U'
            
            # save comment to the database
            comment = BugComment(bugid_id = pk, comment=comment_text, commentauthor_id = request.user.id, author_status = user_status)
            comment.save()
            
        
            response_data = {}
            
            response_data['comment_text'] = comment_text
            response_data['bug_id'] = pk
            response_data['user_id'] = request.user.id
            response_data['created_date'] = created_date
            response_data['username'] = request.user.username
            response_data['user_type'] = user_status
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
        comments = BugComment.objects.filter(bugid=pk)
        
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
   
    
@login_required   
def upvote(request):
    
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
