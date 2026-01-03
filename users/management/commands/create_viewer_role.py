from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Post
from events.models import Event


class Command(BaseCommand):
    help = 'Create Viewer role group'

    def handle(self, *args, **kwargs):
        viewer_group, created = Group.objects.get_or_create(name='Viewer')
        
        if created:
            post_ct = ContentType.objects.get_for_model(Post)
            event_ct = ContentType.objects.get_for_model(Event)
            
            view_post = Permission.objects.get(content_type=post_ct, codename='view_post')
            view_event = Permission.objects.get(content_type=event_ct, codename='view_event')
            
            viewer_group.permissions.add(view_post, view_event)
            
            self.stdout.write(self.style.SUCCESS('Viewer role created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Viewer role already exists'))
