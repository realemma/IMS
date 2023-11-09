from django.urls import path

from .import views

urlpatterns = [
    path('', views.login, name ='login'), 
    path('signup', views.register, name ='register'), 
    path('logout', views.logout, name ='logout'), 
    path('delete/<int:pk>', views.delete, name ='delete'), 
    path('record', views.record, name ='record'), 
    path('edit_note/<slug:slug>/', views.edit_note, name ='edit_note'),
    path('delete_note/<slug:slug>/', views.delete_note, name ='delete_note'),
    path('update', views.Update, name ='update') 

]