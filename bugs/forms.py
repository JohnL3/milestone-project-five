from django import forms
from .models import Bug, BugComment


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ( "bug_title", "initial_comment")
        
        
class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ["comment", "created_date"]
        widgets = {
            'comment': forms.Textarea(attrs={
                'id': 'comment-text',
                'required': True,
                'placeholder': 'Detail your issue here...'
            }),
            'created_date': forms.TextInput(attrs={
                'id': 'date-comment',
                'type': 'hidden'
            })
        }
        
        
        
        
