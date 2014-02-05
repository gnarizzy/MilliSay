from django import forms
import datetime
from readwrite.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=200, help_text="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), help_text="Content")
    words = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    pub_date = forms.DateTimeField(widget=forms.HiddenInput(),initial=datetime.datetime.now())

#Prevents junk posts
    def clean_content(self):
        content = self.cleaned_data['content']
        length = len(content.split())
        if length < 7:
            raise forms.ValidationError("It looks like you're trying to post junk. Please don't do that.")
        return content

    class Meta:
        model = Post
        fields = ('title', 'content','words','pub_date')

