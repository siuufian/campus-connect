from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Notification(models.Model):
    """
    Notification model to track user notifications for various activities
    """
    NOTIFICATION_TYPES = (
        ('post', 'New Post'),
        ('comment', 'New Comment'),
        ('like', 'Post Liked'),
        ('event_registration', 'Event Registration'),
        ('event_reminder', 'Event Reminder'),
        ('mention', 'Mentioned in Post'),
    )
    
    recipient = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='notifications'
    )
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='sent_notifications',
        null=True,
        blank=True
    )
    notification_type = models.CharField(
        max_length=30, 
        choices=NOTIFICATION_TYPES
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    link = models.CharField(max_length=500, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', '-created_at']),
            models.Index(fields=['recipient', 'is_read']),
        ]
    
    def __str__(self):
        return f"{self.notification_type} - {self.recipient.username}"
    
    def mark_as_read(self):
        """Mark this notification as read"""
        if not self.is_read:
            self.is_read = True
            self.save(update_fields=['is_read'])
    
    def get_absolute_url(self):
        """Return the link associated with this notification"""
        return self.link if self.link else reverse('notification-list')
