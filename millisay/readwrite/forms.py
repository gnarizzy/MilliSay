from django import forms
from readwrite.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Please enter a title.")
    content = forms.CharField(help_text="Please enter your post's content.")

    class Meta:
        model = Post
        fields = ('title', 'content')
