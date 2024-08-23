from django.shortcuts import render,redirect
from manager.models import manager_login
from reception.models import receptionist
from reception.models import guest_entries

# Create your views here.

def manager(request):
    if request.session.get('muser'):
        return redirect('home')
    else:
        return render(request,'manager.html')
    
def mlogin(request):
    muser=request.POST['muser']
    mpass=request.POST['mpass']
    
    res = manager_login.objects.filter(muser=muser, mpass=mpass)
    
    if len(res)==1:
        request.session['muser'] = res[0].muser
        return redirect('home')        
    else:
        return render(request,'manager.html',{'error':'Username or Password is Incorrect!!!'})

def home(request):
    if request.session.get('muser'):
        return render(request,'home.html')
    else:
        return redirect('/manager/')

def logout(request):
    del request.session['muser']
    return redirect('/manager/')
    
def account(request):
    if request.session.get('muser'):
        return render(request,'account.html')
    else:
        return redirect('/manager/')
def create_account(request):
    ruser = request.POST['ruser']
    rname = request.POST['rname']
    rmail = request.POST['rmail']
    rcontact = request.POST['rcontact']
    rpass = request.POST['rpass']
    
    res = receptionist.objects.filter(ruser=ruser)
    
    if len(res)>0:
        return render(request,'account.html',{'msg':'Receptionist is aready exits with th username'})
    else:
        q = receptionist(ruser=ruser,rname=rname,rmail=rmail,rcontact=rcontact,rpass=rpass) 
        q.save()
        return render(request,'account.html',{'msg':'Account Created Succesfully!!!'})

def check(request):
    if request.session.get('muser'):
        res=guest_entries.objects.all()
        return render(request,'check.html',{'res':res})
    else:
        return redirect('/manager/')