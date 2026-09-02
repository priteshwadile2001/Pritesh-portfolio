from django.contrib import admin
from django.urls import path,include
from .views import Signup,Login,ActivateAccountView,Logout

urlpatterns = [
    path('signup/',Signup,name='signup'),
    
    path('login/',Login,name='login'),
    # path('logout/',Signup,name='logout'),
    path('logout/', Logout, name='logout'),
    path('activate/<uidb64>/<token>',ActivateAccountView.as_view(),name='activate')
]
