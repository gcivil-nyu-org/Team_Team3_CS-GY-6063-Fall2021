from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import ThreadModel, MessageModel
from events.models import Event, EventRegistration
from .forms import ThreadForm, MessageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CreateThread(View):


  def get(self, request, *args, **kwargs):
    form = ThreadForm()
    context = {
      'form': form
    }
    return render(request, 'messaging/create_thread.html', context)

  def post(self, request, *args, **kwargs):
    form = ThreadForm(request.POST)
    username = request.POST.get('username')
    
    
    if User.objects.filter(username=username).exists(): 
      receiver = User.objects.get(username=username)

      if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
        thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
        return redirect('thread', pk=thread.pk)
      elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
        thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
        return redirect('thread', pk=thread.pk)
      else: 
        attendees_dupes = []
        attendees = []
        for er in EventRegistration.objects.filter(user = request.user):
          for er2 in EventRegistration.objects.filter(event = er.event).exclude(user = request.user):
            attendees_dupes.append(er2.user)
            [attendees.append(x) for x in attendees_dupes if x not in attendees]
        for e in Event.objects.filter(owner = request.user):
          for er in EventRegistration.objects.filter(event = e).exclude(user = request.user):
            attendees_dupes.append(er.user)
            [attendees.append(x) for x in attendees_dupes if x not in attendees] 

        if receiver in attendees and form.is_valid():
          thread = ThreadModel(
          user=request.user,
          receiver=receiver
          )
          thread.save()
          return redirect('thread', pk=thread.pk)
        else: 
          messages.error(request, 'User is not in your squad!')
          return redirect('create-thread')
    else:
      messages.error(request, 'Invalid username!')
      return redirect('create-thread')

@method_decorator(login_required, name='dispatch')        
class ListThreads(View):

  def get(self, request, *args, **kwargs):
    threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    context = {
        'threads': threads
        }
    return render(request, 'messaging/inbox.html', context)

class CreateMessage(View):

  def post(self, request, pk, *args, **kwargs):
    thread = ThreadModel.objects.get(pk=pk)
    if thread.receiver == request.user:
      receiver = thread.user
    else:
      receiver = thread.receiver
    
    message = MessageModel(
        thread=thread,
        sender_user=request.user,
        receiver_user=receiver,
        body=request.POST.get('message'),
    )
    message.save()
    return redirect('thread', pk=pk)

@method_decorator(login_required, name='dispatch')
class ThreadView(View):
  def get(self, request, pk, *args, **kwargs):
    form = MessageForm()
    thread = ThreadModel.objects.get(pk=pk)
    message_list = MessageModel.objects.filter(thread__pk__contains=pk)
    context = {
      'thread': thread,
      'form': form,
      'message_list': message_list
    }
    return render(request, 'messaging/thread.html', context)
