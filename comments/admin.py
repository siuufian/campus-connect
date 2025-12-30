from django.contrib import admin
from .models import Comment, CommentVote


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'content_preview', 'created_at', 'vote_score']
    list_filter = ['created_at', 'post']
    search_fields = ['author__username', 'content', 'post__title']
    raw_id_fields = ['author', 'post', 'parent']

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'


@admin.register(CommentVote)
class CommentVoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'vote_type', 'created_at']
    list_filter = ['vote_type', 'created_at']
    search_fields = ['user__username', 'comment__content']
    raw_id_fields = ['user', 'comment']
