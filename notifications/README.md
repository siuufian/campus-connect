# Notifications System Documentation

## Overview
The Notifications System is a fully modular Django app that provides real-time notifications for various user activities in the Campus Connect platform.

## Features
- ✅ Real-time notification badges in navbar
- ✅ Comprehensive notification list with pagination
- ✅ AJAX-powered mark as read functionality
- ✅ Multiple notification types (posts, events, comments, likes, mentions)
- ✅ Automatic notifications via Django signals
- ✅ Admin interface for notification management
- ✅ Responsive design with animations
- ✅ Context processor for global unread count

## Installation

### 1. The app is already installed in your project
The `notifications` app is already added to `INSTALLED_APPS` in `settings.py`.

### 2. Run Migrations
```bash
python manage.py makemigrations notifications
python manage.py migrate notifications
```

### 3. URLs are already configured
Notifications URLs are included in the main `urls.py` at `/notifications/`.

## Usage

### Accessing Notifications
- Click the bell icon 🔔 in the navbar to view all notifications
- Unread count badge shows on the bell icon
- Notifications page: `/notifications/`

### Notification Types
1. **post** - New blog post created
2. **comment** - New comment on a post (ready for future implementation)
3. **like** - Someone liked your post (ready for manual triggering)
4. **event_registration** - User registered for an event
5. **event_reminder** - Reminder for upcoming events (ready for cron job)
6. **mention** - User mentioned in a post (ready for future implementation)

## Automatic Notifications

### Already Implemented
The following notifications are triggered automatically via signals:

#### 1. New Post Notifications
When a user creates a blog post, all users (up to 50) receive a notification.
```python
# Triggered in: notifications/signals.py
@receiver(post_save, sender=Post)
def notify_on_new_post(...)
```

#### 2. Event Registration Notifications
When a user registers for an event:
- Event organizer receives a notification
- Registering user receives a confirmation
```python
# Triggered in: notifications/signals.py
@receiver(post_save, sender=EventParticipant)
def notify_on_event_registration(...)
```

## Manual Notification Triggering

### Using the Helper Function
For custom notifications (like likes), use the helper function in your views:

```python
from notifications.signals import create_notification
from django.urls import reverse

# Example: Notify when someone likes a post
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Toggle like logic here...
    
    # If user liked (not unliked), notify post author
    if post.author != request.user:
        create_notification(
            recipient=post.author,
            sender=request.user,
            notification_type='like',
            title=f'{request.user.username} liked your post',
            message=f'"{post.title}" received a new like',
            link=reverse('post-detail', kwargs={'pk': post.pk})
        )
    
    return redirect('post-detail', pk=pk)
```

## API Endpoints

### AJAX Endpoints
All endpoints require authentication:

1. **Mark as Read** (POST)
   ```
   /notifications/mark-read/<id>/
   Returns: {success: true, unread_count: N}
   ```

2. **Mark All as Read** (POST)
   ```
   /notifications/mark-all-read/
   Returns: {success: true, unread_count: 0}
   ```

3. **Delete Notification** (GET)
   ```
   /notifications/delete/<id>/
   Redirects to notification list
   ```

4. **Get Unread Count** (GET)
   ```
   /notifications/unread-count/
   Returns: {unread_count: N}
   ```

5. **Get Recent Notifications** (GET)
   ```
   /notifications/recent/
   Returns: {notifications: [...], unread_count: N}
   ```

## Admin Interface

Access the admin panel at `/admin/` to:
- View all notifications
- Filter by type, read status, date
- Search by recipient, title, or message
- Manually create/edit/delete notifications

## Future Enhancements

### Comment Notifications
When you implement comments, add to `signals.py`:
```python
from blog.models import Comment

@receiver(post_save, sender=Comment)
def notify_on_new_comment(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.author:
        Notification.objects.create(
            recipient=instance.post.author,
            sender=instance.author,
            notification_type='comment',
            title=f'New comment on "{instance.post.title}"',
            message=f'{instance.author.username} commented: "{instance.content[:50]}..."',
            link=reverse('post-detail', kwargs={'pk': instance.post.pk})
        )
```

### Event Reminders
Set up a cron job or Celery task to send event reminders:
```python
from django.utils import timezone
from datetime import timedelta

def send_event_reminders():
    tomorrow = timezone.now().date() + timedelta(days=1)
    upcoming_events = Event.objects.filter(date=tomorrow)
    
    for event in upcoming_events:
        for participant in event.participants.all():
            create_notification(
                recipient=participant.user,
                sender=None,
                notification_type='event_reminder',
                title=f'Reminder: {event.name} tomorrow',
                message=f'Your event "{event.name}" is scheduled for tomorrow',
                link=reverse('event-detail', kwargs={'pk': event.pk})
            )
```

## Template Tags

Use custom template tags for advanced notification rendering:

```django
{% load notification_tags %}

<!-- Get unread notifications -->
{% get_unread_notifications request.user as unread_notifications %}

<!-- Get unread count -->
{% get_unread_count request.user as count %}

<!-- Get icon for notification type -->
<i class="{% notification_icon notification.notification_type %}"></i>

<!-- Get color for notification type -->
<div style="background: {% notification_color notification.notification_type %}">
```

## Troubleshooting

### Notifications not appearing?
1. Check that signals are loaded: Verify `ready()` method in `apps.py`
2. Verify context processor is added to `TEMPLATES` in `settings.py`
3. Check database: `python manage.py shell` → `from notifications.models import Notification; Notification.objects.all()`

### Badge not updating?
1. Clear browser cache
2. Check that context processor is working
3. Verify JavaScript console for AJAX errors

### Migrations failing?
```bash
python manage.py migrate notifications --fake-initial
```

## Performance Considerations

### Database Queries
- Models use database indexes on `recipient` and `created_at`
- Bulk create is used for multiple notifications
- QuerySets use `select_related()` in admin

### Limiting Notifications
- New post notifications limited to 50 users (configurable in signals.py)
- Pagination set to 20 notifications per page (configurable in views.py)

### Optimization Tips
```python
# In signals.py, adjust the limit:
for user in users_to_notify[:50]  # Change 50 to your desired limit

# In views.py, adjust pagination:
paginator = Paginator(notifications, 20)  # Change 20 to your desired page size
```

## File Structure
```
notifications/
├── __init__.py
├── admin.py              # Admin interface configuration
├── apps.py               # App configuration with signal loading
├── context_processors.py # Global unread count context
├── models.py             # Notification model
├── signals.py            # Signal handlers for auto-notifications
├── urls.py               # URL routing
├── views.py              # View functions and AJAX endpoints
├── migrations/
│   └── __init__.py
├── templates/
│   └── notifications/
│       └── notification_list.html  # Main notifications page
└── templatetags/
    ├── __init__.py
    └── notification_tags.py  # Custom template tags

```

## Support
For issues or questions about the notification system, check:
1. Django admin logs
2. Browser console for JavaScript errors
3. Django debug toolbar for query analysis
4. Application logs for signal errors

---

**Version:** 1.0  
**Last Updated:** December 2024  
**Compatible with:** Django 4.x, 5.x
