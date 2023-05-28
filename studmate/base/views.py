from django.shortcuts import render
from .models import Room

# Create your views here.
rooms = [
    {'id':1, 'name':'Let\'s learn Django'},
    {'id':2, 'name':'Let\'s Chill with Python'},
    {'id':3, 'name':'Let\'s learn JS'}
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, id):
    room = Room.objects.get(id=id)
    for i in rooms:
        if i['id'] == int(id):
            room = i
    
    context = {'room': room}
    
    return render(request, 'base/room.html',context)