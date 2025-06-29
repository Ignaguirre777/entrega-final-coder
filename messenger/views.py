from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-date_sent')
    return render(request, 'messenger/inbox.html', {'messages': messages})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-date_sent')
    return render(request, 'messenger/sent.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('messenger-inbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/send.html', {'form': form})
