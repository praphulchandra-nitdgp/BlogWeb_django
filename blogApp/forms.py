from django import forms
from .models import PostModel, Comment
from .models import ContactMessage



class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
            model = PostModel
            fields = ('title', 'content', 'image')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True

class PostUpdateForm(forms.ModelForm):
    class Meta:
            model = PostModel
            fields = ('title', 'content', 'image')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False


class PostDeleteForm(forms.ModelForm):
    class Meta:
            model = PostModel
            fields = []

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Add a comment...'}))
    class Meta:
            model = Comment
            fields = ('content',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }