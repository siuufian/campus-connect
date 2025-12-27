"""
Template tags for notifications
"""
from django import template
from notifications.models import Notification

register = template.Library()


@register.simple_tag
def get_unread_notifications(user):
    """
    Get unread notifications for a user
    """
    if user.is_authenticated:
        return Notification.objects.filter(
            recipient=user,
            is_read=False
        ).order_by('-created_at')[:5]
    return []


@register.simple_tag
def get_unread_count(user):
    """
    Get unread notification count for a user
    """
    if user.is_authenticated:
        return Notification.objects.filter(
            recipient=user,
            is_read=False
        ).count()
    return 0


@register.filter
def notification_icon(notification_type):
    """
    Return Font Awesome icon class for notification type
    """
    icons = {
        'post': 'fas fa-file-alt',
        'comment': 'fas fa-comment',
        'like': 'fas fa-heart',
        'event_registration': 'fas fa-calendar-check',
        'event_reminder': 'fas fa-clock',
        'mention': 'fas fa-at',
    }
    return icons.get(notification_type, 'fas fa-bell')


@register.filter
def notification_color(notification_type):
    """
    Return color for notification type
    """
    colors = {
        'post': '#124E66',
        'comment': '#2E7D96',
        'like': '#e74c3c',
        'event_registration': '#04bde2',
        'event_reminder': '#f39c12',
        'mention': '#9b59b6',
    }
    return colors.get(notification_type, '#666')
