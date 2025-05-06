from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('note/new/', views.create_note, name='create_note'),
    path('note/edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('note/delete/<int:pk>/', views.delete_note, name='delete_note'),
]