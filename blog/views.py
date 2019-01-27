from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


def get_posts(request):
    '''Get a list of all posts and render them'''
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    return render(request,'blogposts.html', {'posts': posts})
    
def single_post(request, pk):
    '''Create a view that returns a single post'''
    post = get_object_or_404(Post, pk=pk)
    post.views +=1
    post.save()
    return render(request, 'singlepost.html', {'post': post})
    
   
def create_edit_post(request, pk=None):
    '''Create or edit a post'''
    
    if not request.user or request.user.is_superuser or request.user.is_staff:
        post = get_object_or_404(Post, pk=pk) if pk else None
        if request.method == 'POST':
            if request.user.is_superuser:
                form = BlogPostForm(request.POST, request.FILES, instance=post)
                if form.is_valid():
                    post=form.save()
                    return redirect(single_post, post.pk)
            else:
                form = BlogPostForm(instance=post)
                
                return render(request, 'blogform.html', {'form': form})
                
        else:
            form = BlogPostForm(instance=post)
            
            return render(request, 'blogform.html', {'form': form})
    else:
        return redirect(reverse('get_posts'))
    
        
