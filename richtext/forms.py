from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')
    content = forms.CharField(label='内容', widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'