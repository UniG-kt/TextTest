from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib import messages

def post(request):
    post_form = PostForm(request.POST or None)
    if post_form.is_valid():
        post_form.save()
        messages.success(request, '成功しました')
    return render(request, 'richtext/post.html', context={
        'post_form': post_form,
    })
