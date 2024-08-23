from django.shortcuts import render,redirect
from . models import receptionist
from . models import guest_entries
import datetime

# Create your views here.

def reception(request):
    if  request.session.get('ruser'):
        return redirect('rhome')
    else:
        return render(request,'reception.html')

def rlogin(request):
    ruser = request.POST['ruser']
    rpass = request.POST['rpass']
    
    res = receptionist.objects.filter(ruser=ruser, rpass=rpass)
        
    if len(res)==1:
        request.session['ruser'] = res[0].ruser
        return redirect('rhome')        
    else:
        return render(request,'reception.html',
            {'error':'Username or Password is Incorrect!!!'})
def rhome(request):
    if request.session.get('ruser'):
        return render(request,'rhome.html')
    else:
        return redirect('/reception/')
        
def rlogout(request):
    del request.session['ruser']
    return redirect('/reception/')

def enter(request):
    if request.session.get('ruser'):
        return render(request,'enter.html')
    else:
        return redirect('/reception/')

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

def chk_entries(request):
    if request.session.get('ruser'):
        res=guest_entries.objects.all()
        return render(request,'chk_entries.html',{'res':res})
    else:
        return redirect('/reception/')

def exit(request):
    if request.session.get('ruser'):
        res=guest_entries.objects.all()
        return render(request,'exit.html',{'res':res})
    else:
        return redirect('/reception/')

def update_exit(request):
    id=request.GET['id']
    exittime=datetime.datetime.now().replace(microsecond=0)
    res=guest_entries.objects.get(id=id)
    res.exittime=exittime
    res.save()
    return render(request,'exit.html',{'msg':'Exit Updated Succesfully!!!'})