from django import forms
from readwrite.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Please enter a title.")
    content = forms.TextField(help_text="Plese enter your post's content.")

    class Meta:
        model = Post