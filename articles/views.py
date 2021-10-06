from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

def home(request):
    create_article_form = forms.CreateArticleForm(request.POST or None)
    if create_article_form.is_valid():
        create_article_form.save()
        messages.success(request, '投稿しました')
    return render(
        request, 'articles/home.html', context={
            'create_article_form': create_article_form,
        }
    )
