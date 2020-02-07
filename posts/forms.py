from posts.models import Posts
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['autor', 'text', 'imagem']