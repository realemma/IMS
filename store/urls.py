from django.urls import path

from .import views

urlpatterns = [
    path('', views.store, name ='store'),
    path('location', views.location, name ='location'),
    path('location/<slug:slug>/', views.edit_loc, name='edit_loc'),
    path('delete_loc/<slug:slug>/', views.delete_loc, name='delete_loc'),
    path('category', views.category, name ='category'),
    path('category/<slug:slug>/', views.edit_cat, name='edit_cat'),
    path('delete_cat/<slug:slug>/', views.delete_Cat, name='delete_Cat'),
    path('item', views.item, name ='item'),
    path('item/<slug:slug>/', views.edit_Item, name='edit_Item'),
    path('delete_item/<slug:slug>/', views.delete_item, name='delete_item'),
    path('allocate', views.allocate, name ='allocate'),
    path('allocate/<slug:slug>/', views.edit_allocate, name ='edit_allocate'),
    path('delete_allocate/<slug:slug>/', views.delete_allocate, name='delete_allocate'),




]