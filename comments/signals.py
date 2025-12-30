from django.db.models.signals import post_save
from django.dispatch import receiver
from comments.models import Comment
from notifications.models import Notification


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        comment = instance
        
        if comment.parent:
            if comment.author != comment.parent.author:
                Notification.objects.get_or_create(
                    recipient=comment.parent.author,
                    sender=comment.author,
                    notification_type='reply',
                    title=f'{comment.author.username} replied to your comment',
                    message=f'{comment.author.username} replied: "{comment.content[:50]}..."',
                    link=f'/post/{comment.post.id}/',
                    defaults={'is_read': False}
                )
        else:
            if comment.author != comment.post.author:
                Notification.objects.get_or_create(
                    recipient=comment.post.author,
                    sender=comment.author,
                    notification_type='comment',
                    title=f'{comment.author.username} commented on your post',
                    message=f'{comment.author.username} commented: "{comment.content[:50]}..."',
                    link=f'/post/{comment.post.id}/',
                    defaults={'is_read': False}
                )
