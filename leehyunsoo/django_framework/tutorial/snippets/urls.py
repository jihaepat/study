from django.conf.urls import url
from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<pk>/', views.SnippetDetail.as_view()),
    re_path(r'^snippets/$', views.SnippetList.as_view()),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)