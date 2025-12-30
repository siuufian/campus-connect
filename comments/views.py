from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from blog.models import Post
from .models import Comment, CommentVote
from .forms import CommentForm


@login_required
@require_POST
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        
        parent_id = request.POST.get('parent_id')
        if parent_id:
            comment.parent = get_object_or_404(Comment, pk=parent_id)
        
        comment.save()
    
    return redirect('post-detail', pk=pk)


@login_required
@require_POST
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
    
    return redirect('post-detail', pk=post_pk)


@login_required
@require_POST
def vote_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    vote_type = request.POST.get('vote_type')
    
    if vote_type not in ['upvote', 'downvote']:
        return JsonResponse({'error': 'Invalid vote type'}, status=400)
    
    vote, created = CommentVote.objects.get_or_create(
        comment=comment,
        user=request.user,
        defaults={'vote_type': vote_type}
    )
    
    if not created:
        if vote.vote_type == vote_type:
            vote.delete()
            removed = True
        else:
            vote.vote_type = vote_type
            vote.save()
            removed = False
    else:
        removed = False
    
    return JsonResponse({
        'upvotes': comment.upvote_count,
        'downvotes': comment.downvote_count,
        'score': comment.vote_score,
        'removed': removed
    })
