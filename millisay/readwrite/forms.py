from django import forms
from readwrite.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=200, help_text="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), help_text="Content")
    #Create hidden field for word count?
    class Meta:
        model = Post
        fields = ('title', 'content')
