from django import forms
from django.contrib.auth.models import User
from djnycapp.models import Post
from djnycapp.fields import UserAutoCompleteField


USERS = (
    ('', '--'),
    ('jlilly', 'Justin Lilly'),
    ('test', 'Test User'),
    )

class PostForm(forms.ModelForm):
    name = forms.CharField()
    body = forms.Textarea()
    author =  UserAutoCompleteField()

    class Meta:
        model = Post
        fields = ['name', 'body', 'author']
