from django.urls import path
from . import views

app_name = 'richtext'

urlpatterns = [
    path('post', views.post, name='post'),
]