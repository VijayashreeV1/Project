from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contacts, name='view_contacts'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:id>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
]