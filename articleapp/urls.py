from django.urls import path
from django.views.generic import TemplateView
from articleapp.views import ArticleCreateView,ArticleDetailView, ArticleListView,ArticleUpdateView,ArticleDeleteView

app_name = 'articleapp'

urlpatterns = [
    #list
    path('list/', ArticleListView.as_view(), name='list'),
    #create
    path('create/', ArticleCreateView.as_view(), name='create'),
    #detail
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    #update
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    #delete
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]