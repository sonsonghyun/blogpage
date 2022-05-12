
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from articleapp.views import ArticleListView

urlpatterns = [
    path('',ArticleListView.as_view(), name='home'),
    #admin page
    path('admin/', admin.site.urls),
    #accountapp
    path('accounts/', include('accountapp.urls')),
    #profileapp
    path('profiles/', include('profileapp.urls')),
    #articlesapp
    path('articles/', include('articleapp.urls')),
    #commentapp
    path('comments/', include('commentapp.urls')),
    #projectapp
    path('projects/',include('projectapp.urls')),
    #subscribeapp
    path('subscribe/',include('subscribeapp.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
