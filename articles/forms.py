from django import forms
from django.db.models import fields
from .models import Articles

class CreateArticleForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Description', 'rows': 10, 'cols': 60}))

    class Meta:
        model = Articles
        fields = ('title', 'description', )