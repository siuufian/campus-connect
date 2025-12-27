"""
Management command to create test notifications
Usage: python manage.py create_test_notifications --username=admin --count=5
"""
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.urls import reverse
from notifications.models import Notification
from random import choice


class Command(BaseCommand):
    help = 'Create test notifications for a user'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            required=True,
            help='Username of the recipient',
        )
        parser.add_argument(
            '--count',
            type=int,
            default=5,
            help='Number of test notifications to create',
        )

    def handle(self, *args, **options):
        username = options['username']
        count = options['count']
        
        try:
            recipient = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f'User "{username}" does not exist')
        
        # Create test notifications
        notification_types = ['post', 'comment', 'like', 'event_registration', 'event_reminder']
        
        test_messages = {
            'post': ('New post available', 'Check out the latest blog post'),
            'comment': ('New comment', 'Someone commented on your post'),
            'like': ('Post liked', 'Your post received a new like'),
            'event_registration': ('Event registration', 'New registration for your event'),
            'event_reminder': ('Event reminder', 'Your event is coming up soon'),
        }
        
        created_count = 0
        for i in range(count):
            notif_type = choice(notification_types)
            title, message = test_messages[notif_type]
            
            Notification.objects.create(
                recipient=recipient,
                sender=None,
                notification_type=notif_type,
                title=f'{title} #{i+1}',
                message=f'{message} (Test notification)',
                link='/',
                is_read=False
            )
            created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} test notifications for {username}'
            )
        )
