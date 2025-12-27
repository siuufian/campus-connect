from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse

# Import models (we'll handle circular imports safely)
from blog.models import Post
from events.models import EventParticipant

from .models import Notification

@receiver(post_save, sender=Post)
def notify_on_new_post(sender, instance, created, **kwargs):
    """
    Send notification to all followers when a new post is created
    (For now, we'll notify all users except the author)
    """
    if created:
        # Get all users except the post author
        users_to_notify = User.objects.exclude(id=instance.author.id)
        
        # Create notifications for each user
        notifications = [
            Notification(
                recipient=user,
                sender=instance.author,
                notification_type='post',
                title=f'New post by {instance.author.username}',
                message=f'{instance.author.username} published: "{instance.title}"',
                link=reverse('post-detail', kwargs={'pk': instance.pk})
            )
            for user in users_to_notify[:50]  # Limit to first 50 users for performance
        ]
        
        # Bulk create for better performance
        Notification.objects.bulk_create(notifications)

@receiver(post_save, sender=EventParticipant)
def notify_on_event_registration(sender, instance, created, **kwargs):
    """
    Notify event organizer when someone registers for their event
    """
    if created:
        event = instance.event
        organizer = event.organizer
        
        # Don't notify if organizer registered for their own event
        if organizer != instance.user:
            Notification.objects.create(
                recipient=organizer,
                sender=instance.user,
                notification_type='event_registration',
                title=f'New registration for {event.name}',
                message=f'{instance.user.username} registered for your event "{event.name}"',
                link=reverse('event-detail', kwargs={'pk': event.pk})
            )
        
        # Also notify the user who registered
        Notification.objects.create(
            recipient=instance.user,
            sender=None,
            notification_type='event_registration',
            title=f'Registration confirmed',
            message=f'You successfully registered for "{event.name}"',
            link=reverse('event-detail', kwargs={'pk': event.pk})
        )

# Note: Comment notifications will be added when comments feature is implemented
# For now, this provides the infrastructure

# To add comment notifications later, you would add:
# from blog.models import Comment (when Comment model exists)
# @receiver(post_save, sender=Comment)
# def notify_on_new_comment(sender, instance, created, **kwargs):
#     if created:
#         # Notify post author
#         if instance.post.author != instance.author:
#             Notification.objects.create(
#                 recipient=instance.post.author,
#                 sender=instance.author,
#                 notification_type='comment',
#                 title=f'New comment on "{instance.post.title}"',
#                 message=f'{instance.author.username} commented on your post',
#                 link=reverse('post-detail', kwargs={'pk': instance.post.pk})
#             )

def create_notification(recipient, sender, notification_type, title, message, link=None):
    """
    Helper function to create notifications programmatically
    Use this in views when you need to trigger custom notifications
    
    Example:
        from notifications.signals import create_notification
        create_notification(
            recipient=user,
            sender=request.user,
            notification_type='like',
            title='Someone liked your post',
            message=f'{request.user.username} liked your post',
            link=post_url
        )
    """
    return Notification.objects.create(
        recipient=recipient,
        sender=sender,
        notification_type=notification_type,
        title=title,
        message=message,
        link=link
    )
