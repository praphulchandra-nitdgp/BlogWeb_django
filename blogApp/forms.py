from django import forms
from .models import PostModel, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
            model = PostModel
            fields = ('title', 'content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
            model = PostModel
            fields = ('title', 'content')

class PostDeleteForm(forms.ModelForm):
    class Meta:
            model = PostModel
            fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Add a comment...'}))
    class Meta:
            model = Comment
            fields = ('content',)