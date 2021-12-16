from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import StudentReg
from .models import User

# Create your views here.
#this function will add betw items and show new items...........................................................


def add_show(request):
    if request.method=='POST':
        fm=StudentReg(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pw=fm.cleaned_data['password']
           ct=fm.cleaned_data['city']
           ag=fm.cleaned_data['age']
           ph=fm.cleaned_data['phone']
           reg=User(name=nm,email=em,password=pw,city=ct,age=ag,phone=ph)
           reg.save()
           fm=StudentReg()
           stud=User.objects.all()
           return render(request,'enroll/gives.html',{'formx':fm,'stu':stud })
        else:
           return render(request,'enroll/addandshow.html')   
    else:
        fm=StudentReg()
        stud=User.objects.all()
        return render(request,'enroll/addandshow.html',{'formx':fm,'stu':stud })


#separately implemenating one by one data in database is done directly in simpler manner over here ......#
    """
       
if fm.is_valid():
            fm.save()

    """

#this function will delete................................................................................



def deleteCrd(request,id):
    if request.method=='POST':
        dlt=User.objects.get(pk=id)
        dlt.delete()
        return HttpResponseRedirect('/') 


def updateCrd(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentReg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentReg(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
    


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        ctr = User.objects.filter(name__icontains=q).order_by("-id")
    return render(request, 'enroll/search.html', {'ct': ctr})


def gives(request):
    stud=User.objects.all().order_by("-id")
    return render(request,'enroll/gives.html',{'stu':stud })