# Testing the Notifications System

## Quick Start Testing

### 1. Run Migrations
```bash
python manage.py makemigrations notifications
python manage.py migrate notifications
```

### 2. Create Test Notifications
```bash
# Replace 'admin' with your actual username
python manage.py create_test_notifications --username=admin --count=10
```

### 3. Access Notifications
- Login to your account
- Click the bell icon 🔔 in the navbar
- You should see 10 test notifications

## Automated Testing

### Test New Post Notifications
1. Login to the site
2. Create a new blog post
3. Login as a different user
4. Check notifications - you should see a notification about the new post

### Test Event Registration Notifications
1. Login as User A
2. Create a new event
3. Login as User B
4. Register for the event
5. Login back as User A
6. Check notifications - you should see registration confirmation
7. Login back as User B
8. Check notifications - you should see registration confirmation

### Test Mark as Read
1. Go to notifications page
2. Click the check mark button on any unread notification
3. The notification should be marked as read (loses the "New" badge)
4. The unread count in the navbar should decrease

### Test Mark All as Read
1. Have multiple unread notifications
2. Click "Mark All as Read" button
3. All notifications should be marked as read
4. The navbar badge should disappear

### Test Delete Notification
1. Go to notifications page
2. Click the trash icon on any notification
3. Confirm the deletion
4. The notification should be removed

### Test Notification Links
1. Click on the external link icon on a notification
2. You should be redirected to the relevant post/event
3. The notification should be marked as read automatically

## Manual Testing Checklist

- [ ] Navbar bell icon appears for authenticated users
- [ ] Unread count badge displays correctly
- [ ] Badge animates (pulse effect)
- [ ] Clicking bell navigates to notification list
- [ ] Notifications display with correct icons and colors
- [ ] Pagination works (if more than 20 notifications)
- [ ] "New" badge shows on unread notifications
- [ ] Mark as read button works (AJAX)
- [ ] Mark all as read works (page reload)
- [ ] Delete notification works (confirmation dialog)
- [ ] External links work and mark notification as read
- [ ] Empty state shows when no notifications exist
- [ ] New post creates notifications for other users
- [ ] Event registration creates notifications for both parties
- [ ] Admin panel shows notifications correctly
- [ ] Filtering and searching work in admin
- [ ] Context processor provides unread count globally

## Testing Different Notification Types

### Post Notifications
```bash
# Create a test post notification
python manage.py shell
```
```python
from django.contrib.auth.models import User
from notifications.signals import create_notification
from django.urls import reverse

recipient = User.objects.get(username='your_username')
sender = User.objects.get(username='another_user')

create_notification(
    recipient=recipient,
    sender=sender,
    notification_type='post',
    title='Test Post Notification',
    message='This is a test notification for a new post',
    link=reverse('blog-home')
)
```

### Event Notifications
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
from notifications.signals import create_notification
from django.urls import reverse

recipient = User.objects.get(username='your_username')

create_notification(
    recipient=recipient,
    sender=None,
    notification_type='event_reminder',
    title='Event Tomorrow',
    message='Your event "Django Workshop" is scheduled for tomorrow',
    link=reverse('event-list')
)
```

### Like Notifications (for future implementation)
```python
# In your blog views.py, add this to the like_post function:
from notifications.signals import create_notification

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        
        # Send notification to post author
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

## Database Verification

### Check Notifications in Database
```bash
python manage.py shell
```
```python
from notifications.models import Notification

# View all notifications
print(f"Total notifications: {Notification.objects.count()}")

# View unread notifications
print(f"Unread: {Notification.objects.filter(is_read=False).count()}")

# View notifications by type
from django.db.models import Count
types = Notification.objects.values('notification_type').annotate(count=Count('id'))
for t in types:
    print(f"{t['notification_type']}: {t['count']}")

# View recent notifications for a specific user
from django.contrib.auth.models import User
user = User.objects.get(username='your_username')
recent = Notification.objects.filter(recipient=user)[:5]
for n in recent:
    print(f"[{'✓' if n.is_read else '✗'}] {n.title}")
```

## Performance Testing

### Load Testing
```bash
# Create many notifications to test pagination
python manage.py create_test_notifications --username=admin --count=100
```

### Database Query Testing
```bash
python manage.py shell
```
```python
from django.db import connection
from django.test.utils import override_settings
from notifications.models import Notification

# Enable query logging
from django.db import reset_queries
from django.conf import settings
settings.DEBUG = True

# Perform an operation
notifications = Notification.objects.filter(recipient__username='admin')[:20]
list(notifications)  # Force evaluation

# Check queries
from django.db import connection
print(f"Number of queries: {len(connection.queries)}")
for query in connection.queries:
    print(query['sql'])
```

## Troubleshooting Common Issues

### Notifications not appearing?
```bash
# Check if signals are loaded
python manage.py shell
```
```python
from django.apps import apps
app = apps.get_app_config('notifications')
print(f"App ready: {app.ready}")

# Check signal connections
from django.db.models.signals import post_save
print("Connected signals:")
for receiver in post_save._live_receivers(None):
    print(receiver)
```

### Context processor not working?
```bash
# Verify it's in settings
python manage.py shell
```
```python
from django.conf import settings
processors = settings.TEMPLATES[0]['OPTIONS']['context_processors']
print('notifications.context_processors.unread_notifications' in processors)
```

### Badge not updating after marking as read?
Check browser console for JavaScript errors and ensure CSRF token is being sent correctly.

## Cleanup After Testing

### Delete Test Notifications
```bash
python manage.py shell
```
```python
from notifications.models import Notification

# Delete all test notifications
Notification.objects.filter(message__contains='Test notification').delete()

# Or delete all notifications for a user
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
Notification.objects.filter(recipient=user).delete()
```

### Cleanup Old Notifications
```bash
# Dry run to see what would be deleted
python manage.py cleanup_notifications --days=30 --dry-run

# Actually delete
python manage.py cleanup_notifications --days=30
```

## Expected Results

After following all tests:
1. ✅ All notification types work correctly
2. ✅ AJAX endpoints respond properly
3. ✅ UI updates without page refresh
4. ✅ Database queries are optimized
5. ✅ No JavaScript errors in console
6. ✅ No Django errors in server logs
7. ✅ Notifications persist across sessions
8. ✅ Admin interface is fully functional

## Report Issues

If any test fails, check:
1. Django server logs
2. Browser console
3. Network tab in DevTools (for AJAX calls)
4. Database state (`python manage.py dbshell`)
