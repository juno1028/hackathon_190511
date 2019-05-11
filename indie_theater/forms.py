from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class ViewForm(forms.ModelForm): #ModelForm 임을 알려주는 구문.
    class Meta:
        model = Post
        fields = ('title', 'content', 'director', 'rating1', 'rating2', 'rating3', 'img',  'created_date',  )

class CfForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'director', 'created_date', 'img',  )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'content' , )

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
