from django import forms
from readwrite.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=200, help_text="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), help_text="Content")
    words = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Post
        fields = ('title', 'content','words')
