"""
Management command to clean up old read notifications
Usage: python manage.py cleanup_notifications --days=30
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from notifications.models import Notification


class Command(BaseCommand):
    help = 'Delete read notifications older than specified days (default: 30)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help='Delete read notifications older than this many days',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )

    def handle(self, *args, **options):
        days = options['days']
        dry_run = options['dry_run']
        
        cutoff_date = timezone.now() - timedelta(days=days)
        
        # Get notifications to delete
        old_notifications = Notification.objects.filter(
            is_read=True,
            created_at__lt=cutoff_date
        )
        
        count = old_notifications.count()
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    f'DRY RUN: Would delete {count} read notifications older than {days} days'
                )
            )
            return
        
        if count == 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'No read notifications older than {days} days found'
                )
            )
            return
        
        # Delete the notifications
        old_notifications.delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully deleted {count} read notifications older than {days} days'
            )
        )
