from django import forms

from .models import Post # type: ignore
from .models import Blogs # type: ignore

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'img', 'description', 'authName']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'description', 'authName', 'img']
