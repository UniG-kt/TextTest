from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Post

class PostAdminForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')
    content = forms.CharField(label='内容', widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
