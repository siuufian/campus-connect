from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:pk>/', views.add_comment, name='add-comment'),
    path('delete/<int:pk>/', views.delete_comment, name='delete-comment'),
    path('vote/<int:pk>/', views.vote_comment, name='vote-comment'),
]
