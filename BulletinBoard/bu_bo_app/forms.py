from django import forms
from .models import Article, UserResponse


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'upload'] #автора убрал, он автозаполняется во вьюсе


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['text', ]  #автора и статью убрал, они автозаполняются во вьюсе

