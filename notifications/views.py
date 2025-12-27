from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from .models import Notification

@login_required
def notification_list(request):
    """
    Display all notifications for the logged-in user
    """
    notifications = Notification.objects.filter(recipient=request.user)
    
    # Pagination
    paginator = Paginator(notifications, 20)  # 20 notifications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unread count
    unread_count = notifications.filter(is_read=False).count()
    
    context = {
        'notifications': page_obj,
        'unread_count': unread_count,
        'page_obj': page_obj,
    }
    
    return render(request, 'notifications/notification_list.html', context)

@login_required
@require_POST
def mark_as_read(request, pk):
    """
    Mark a single notification as read (AJAX endpoint)
    """
    notification = get_object_or_404(
        Notification, 
        pk=pk, 
        recipient=request.user
    )
    notification.mark_as_read()
    
    # Get updated unread count
    unread_count = Notification.objects.filter(
        recipient=request.user, 
        is_read=False
    ).count()
    
    return JsonResponse({
        'success': True,
        'unread_count': unread_count
    })

@login_required
@require_POST
def mark_all_as_read(request):
    """
    Mark all notifications as read for the logged-in user
    """
    Notification.objects.filter(
        recipient=request.user, 
        is_read=False
    ).update(is_read=True)
    
    return JsonResponse({
        'success': True,
        'unread_count': 0
    })

@login_required
def delete_notification(request, pk):
    """
    Delete a single notification
    """
    notification = get_object_or_404(
        Notification, 
        pk=pk, 
        recipient=request.user
    )
    notification.delete()
    
    return redirect('notification-list')

@login_required
def get_unread_count(request):
    """
    Get unread notification count (AJAX endpoint)
    """
    unread_count = Notification.objects.filter(
        recipient=request.user, 
        is_read=False
    ).count()
    
    return JsonResponse({
        'unread_count': unread_count
    })

@login_required
def get_recent_notifications(request):
    """
    Get recent notifications for navbar dropdown (AJAX endpoint)
    """
    notifications = Notification.objects.filter(
        recipient=request.user
    )[:5]  # Get 5 most recent
    
    data = [{
        'id': n.id,
        'title': n.title,
        'message': n.message,
        'type': n.notification_type,
        'is_read': n.is_read,
        'link': n.link,
        'created_at': n.created_at.strftime('%B %d, %Y %I:%M %p')
    } for n in notifications]
    
    return JsonResponse({
        'notifications': data,
        'unread_count': Notification.objects.filter(
            recipient=request.user, 
            is_read=False
        ).count()
    })
