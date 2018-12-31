from django import forms
from .models import Post
from django.forms.widgets import ClearableFileInput

class MyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = ""
    clear_checkbox_label = 'Clear'


class BlogPostForm(forms.ModelForm):
    image = forms.ImageField(label='Image',required = False, widget=MyClearableFileInput)
    class Meta:
        model = Post
        fields = ("title", "content", "image", "published_date")
        