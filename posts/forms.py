from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Optional'}),required=False)
    class Meta:
        model=Post
        fields=('title','content','image')

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add a comment...'}),label='')
    class Meta:
        model = Comment
        fields=('body',)