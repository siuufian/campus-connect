# Migration Instructions for Notifications System

## IMPORTANT: Run These Commands in Order

### Step 1: Navigate to Project Directory
```bash
cd C:\Users\abusu\Downloads\Diagram\campus-connect-main
```

### Step 2: Activate Virtual Environment (if using one)
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Step 3: Create Migrations
```bash
python manage.py makemigrations notifications
```

**Expected Output:**
```
Migrations for 'notifications':
  notifications\migrations\0001_initial.py
    - Create model Notification
```

### Step 4: Apply Migrations
```bash
python manage.py migrate notifications
```

**Expected Output:**
```
Operations to perform:
  Apply all migrations: notifications
Running migrations:
  Applying notifications.0001_initial... OK
```

### Step 5: Verify Installation
```bash
python manage.py showmigrations notifications
```

**Expected Output:**
```
notifications
 [X] 0001_initial
```

### Step 6: Create a Superuser (if you don't have one)
```bash
python manage.py createsuperuser
```

### Step 7: Test the System
```bash
# Create test notifications
python manage.py create_test_notifications --username=YOUR_USERNAME --count=5

# Start the development server
python manage.py runserver
```

### Step 8: Access and Verify
1. Open browser: http://127.0.0.1:8000/
2. Login with your credentials
3. Look for the bell icon 🔔 in the navbar
4. Click it to see your notifications

## If You Encounter Issues

### Issue: Migrations already exist
```bash
# If you see "No changes detected"
python manage.py migrate notifications --fake-initial
```

### Issue: Database locked or conflicts
```bash
# Reset migrations (WARNING: This will delete notification data)
python manage.py migrate notifications zero
python manage.py makemigrations notifications
python manage.py migrate notifications
```

### Issue: Context processor not working
Verify in `proj2/settings.py` that this line exists in TEMPLATES:
```python
'notifications.context_processors.unread_notifications',
```

### Issue: Signals not working
Check that `notifications/apps.py` has:
```python
def ready(self):
    import notifications.signals
```

## Rollback Instructions (If Needed)

If you need to remove the notifications system:

### Step 1: Unapply Migrations
```bash
python manage.py migrate notifications zero
```

### Step 2: Remove from Settings
Remove from `INSTALLED_APPS` in `proj2/settings.py`:
```python
'notifications.apps.NotificationsConfig',  # Remove this line
```

Remove from context processors:
```python
'notifications.context_processors.unread_notifications',  # Remove this line
```

### Step 3: Remove URL Configuration
Remove from `proj2/urls.py`:
```python
path('notifications/', include('notifications.urls')),  # Remove this line
```

## Post-Installation Checklist

- [ ] Migrations created successfully
- [ ] Migrations applied without errors
- [ ] Notifications app shows in admin panel
- [ ] Bell icon visible in navbar (when logged in)
- [ ] Test notifications created successfully
- [ ] Clicking bell shows notification list
- [ ] Mark as read works
- [ ] Delete notification works
- [ ] New post creates notifications
- [ ] Event registration creates notifications

## Common Migration Errors and Solutions

### Error: "Table 'notifications_notification' already exists"
**Solution:**
```bash
python manage.py migrate notifications --fake-initial
```

### Error: "No module named 'notifications'"
**Solution:**
Ensure you're in the correct directory and virtual environment is activated.

### Error: "UNIQUE constraint failed"
**Solution:**
This usually means duplicate data. Check your signals aren't creating duplicate notifications.

### Error: "Context processor not found"
**Solution:**
Check the path: `notifications.context_processors.unread_notifications`
Ensure the file exists at: `notifications/context_processors.py`

## Verification Commands

### Check App Installation
```bash
python manage.py shell
```
```python
from django.apps import apps
print(apps.get_app_config('notifications'))
```

### Check Database Tables
```bash
python manage.py dbshell
```
```sql
.tables
-- You should see: notifications_notification

.schema notifications_notification
-- Shows the table structure
```

### Check Signals
```bash
python manage.py shell
```
```python
from blog.models import Post
from events.models import EventParticipant
from django.db.models.signals import post_save

# Check if signals are connected
print(post_save.has_listeners(Post))  # Should be True
print(post_save.has_listeners(EventParticipant))  # Should be True
```

## Success Indicators

You'll know the system is working correctly when:

1. ✅ `python manage.py migrate notifications` runs without errors
2. ✅ Bell icon appears in navbar for logged-in users
3. ✅ Badge shows unread count
4. ✅ Creating a post generates notifications
5. ✅ Registering for an event generates notifications
6. ✅ Admin panel shows Notifications model
7. ✅ No console errors when clicking notifications
8. ✅ AJAX operations work smoothly

## Need Help?

If migrations fail or the system doesn't work:
1. Check Django version: `python manage.py --version`
2. Check installed apps: `python manage.py shell` → `from django.conf import settings; print(settings.INSTALLED_APPS)`
3. Review server logs for errors
4. Check browser console for JavaScript errors
5. Verify database integrity: `python manage.py check`

---

**Ready to proceed?** Run the commands in order starting from Step 1!
