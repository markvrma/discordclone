from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.
# rooms = [
#     {'id':1,'name':'rock'},
#     {'id':2,'name':'avant'},
#     {'id':3,'name':'techno'},
# ]
def home(request):
    context = {'rooms':Room.objects.all()}
    return render(request,'base/home.html',context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html', context)