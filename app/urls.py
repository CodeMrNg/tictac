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
    path('new_ticket/<int:event_id>/', views.new_ticket, name='new_ticket'),
    path('success/', views.success, name='success'),
    path('Ticket_detail/<int:ticket_id>/', views.ticket_detail, name='ticket'),

]