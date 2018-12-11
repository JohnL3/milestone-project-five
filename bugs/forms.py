from django import forms
from .models import Bug, BugComment


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ( "bug_title", "initial_comment")
        
        
class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ("comment")
        
        
        
