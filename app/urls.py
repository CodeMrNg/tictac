from django.urls import path
from . import views



urlpatterns = [

    path('',views.index, name='home'),
    path('dashbord/', views.dash, name = 'dash'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginn, name='login'),
    path('logout/', views.logoutt, name='logout'),
    path('inscription/', views.signup, name='register'),
    path('add_event/', views.addevent, name='add_event'),

]