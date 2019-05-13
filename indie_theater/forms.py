from django import forms
from .models import Post, Comment, CfPost, CfComment
from django.contrib.auth.models import User

class ViewForm(forms.ModelForm): #ModelForm 임을 알려주는 구문.
    class Meta:
        model = Post
        fields = ('title', 'director', 'content', 'img',  'created_date',  )

class CfForm(forms.ModelForm):
    class Meta:
        model = CfPost
        fields = ('title', 'content', 'director', 'duration', 'img',  )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( '내용', '창의성', '시사성', '예술성' )

class CfCommentForm(forms.ModelForm):
    class Meta:
        model = CfComment
        fields = ( 'cfcontent' , )

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
