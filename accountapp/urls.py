

from django.urls import path
from accountapp.views import AccountCreateView,AccountDetailView,AccountUpdateView,AccountDeleteView
from django.contrib.auth.views import LoginView,LogoutView

app_name = "accountapp"

urlpatterns = [
    
    #sign up
    path('create/', AccountCreateView.as_view()  , name='create'),
    #login
    #loginview는 template을 정해줘야 함
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html')  , name='login'),
    #logout
    path('logout/', LogoutView.as_view()  , name='logout'),
    #detail
    path('detail/<int:pk>', AccountDetailView.as_view()  , name='detail'),
    #update
    path('update/<int:pk>', AccountUpdateView.as_view()  , name='update'),
    #delete
    path('delete/<int:pk>', AccountDeleteView.as_view()  , name='delete'),
]
