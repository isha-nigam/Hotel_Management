from django.shortcuts import render
from reception.models import guest_entries
import datetime

# create your views here

def index(request):
    return render(request,'index.html')

def room(request):
    return render(request,'room.html')
def book_now(request):
    return render(request,'book_enter.html')

def insert_entry(request):
    guest_name = request.POST['guest_name']
    guest_num = request.POST['guest_num']
    guest_id = request.POST['guest_id']
    guest_room = request.POST['guest_room']
    address = request.POST['address']
    
    intime=datetime.datetime.now().replace(microsecond=0)
    
    q=guest_entries(guest_name=guest_name,guest_num=guest_num,guest_id=
    guest_id,guest_room=guest_room,address=address,intime=intime)
    
    q.save()
    
    return render(request,'enter.html',{'msg':'Entry Inserted Succesfully!!!'})