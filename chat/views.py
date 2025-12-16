from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Conversation

User = get_user_model()

@login_required
def inbox(request):
    conversations = request.user.conversations.all().order_by('-updated_at')
    
    # Enrich conversations with the "other" user
    for convo in conversations:
        convo.other_user = convo.participants.exclude(id=request.user.id).first()
        
    context = {
        'conversations': conversations
    }
    return render(request, 'chat/inbox.html', context)

@login_required
def room(request, username):
    other_user = get_object_or_404(User, username=username)
    
    # Find or create conversation
    # Complex query to find existing conversation between exactly these two users
    conversations = Conversation.objects.filter(participants=request.user).filter(participants=other_user)
    if conversations.exists():
        conversation = conversations.first()
    else:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)
        
    # Mark messages as read? (Simple implementation for now)
    
    messages = conversation.messages.all().order_by('timestamp')

    context = {
        'room_name': conversation.id,
        'other_user': other_user,
        'messages': messages,
        'chat_history': messages
    }
    return render(request, 'chat/room.html', context)
