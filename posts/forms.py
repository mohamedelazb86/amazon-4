from django import forms
from .models import Review,Post

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['rate','content']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('user',)