"""
Context processor to add unread notification count to all templates
"""
from .models import Notification


def unread_notifications(request):
    """
    Add unread notification count to context for all templates
    """
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()
        return {
            'unread_notifications_count': unread_count
        }
    return {
        'unread_notifications_count': 0
    }
