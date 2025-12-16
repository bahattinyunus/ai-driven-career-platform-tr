from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Connection, Comment

@login_required
def feed(request):
    user = request.user
    
    # Get connected users
    connected_users = Connection.objects.filter(user=user, status='accepted').values_list('connection', flat=True)
    
    # Get posts from self and connections
    posts = Post.objects.filter(
        Q(user__id__in=connected_users) | Q(user=user)
    ).select_related('user').prefetch_related('comments', 'likes').order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')
        if content or image:
            Post.objects.create(user=user, content=content, image=image)
            return redirect('networking:feed')

    context = {
        'posts': posts,
    }
    return render(request, 'networking/feed.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('networking:feed')

@login_required
def network(request):
    # Suggest users to connect with (simple logic: all users except self and already connected)
    user = request.user
    existing_connections = Connection.objects.filter(user=user).values_list('connection', flat=True)
    
    # Imports inside to avoid circular dependency if any
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    suggestions = User.objects.exclude(id=user.id).exclude(id__in=existing_connections)[:20]
    
    context = {
        'suggestions': suggestions
    }
    return render(request, 'networking/network.html', context)
