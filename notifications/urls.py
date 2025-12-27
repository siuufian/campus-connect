from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_list, name='notification-list'),
    path('mark-read/<int:pk>/', views.mark_as_read, name='notification-mark-read'),
    path('mark-all-read/', views.mark_all_as_read, name='notification-mark-all-read'),
    path('delete/<int:pk>/', views.delete_notification, name='notification-delete'),
    path('unread-count/', views.get_unread_count, name='notification-unread-count'),
    path('recent/', views.get_recent_notifications, name='notification-recent'),
]
