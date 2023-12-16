from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.Openai.as_view(), name='chatgpt'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
