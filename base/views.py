from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
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