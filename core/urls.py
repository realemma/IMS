from django.urls import path

from .import views

urlpatterns = [
    path('', views.dashboard, name ='dashboard'),
    path('Uncom/<slug:slug>/', views.Uncom, name ='Uncom'),
    path('pend', views.pend, name ='pend'),
    path('pend_app/<slug:slug>/', views.pend_app, name ='pend_app'),
    path('pend_reject/<slug:slug>/', views.pend_reject, name ='pend_reject'),
    path('approve', views.approve, name ='approve'),
    path('approve_edit/<slug:slug>/', views.approve_edit, name ='approve_edit'),
    path('reject', views.reject, name ='reject'),
    path('reject_edit/<slug:slug>/', views.reject_edit, name ='reject_edit'),


]