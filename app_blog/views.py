from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import product
import os
# Create your views here.
def myhome(request):
    return render(request,'home.html',{'name':'Damo'})

def ContactUs(request):
    concat = {'rooms':'rooms'}
    return render(request,'contactus.html')

# section = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'r u interested in Django Ry8'},
#     {'id':3, 'name':'Yah!!! u r interested in Another FrameWork'},
# ]

def addition(request):
    return render(request, 'addition.html')
    
def add(request):
    no1 = int(request.POST['fno'])
    no2 = int(request.POST['sno'])
    ans = no1+no2
    return render(request,'result.html',{'result':ans})

def add_product(request):
    mydata=product.objects.all()
    context={
        'myvar':mydata,
    }
    return render(request,'add_product.html',context)

def adddata(request):
    if request.method == 'POST':
        myobj = product()
        myobj.product_type = request.POST.get('ptype')
        myobj.product_name = request.POST.get('pname')
        myobj.descr = request.POST.get('desc')
        myobj.price = request.POST.get('price')

        if len(request.FILES)!=0:
            myobj.image = request.FILES['img']

        myobj.save()
        # messages.sucess('request', "item added sucessfully")
    return redirect("/add_product")

    
def editpage(request,pk):
    data = product.objects.get(id=pk)
    context={'myeditdata':data}
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(data.image)>0:
                os.remove(data.image.path)
            data.image=request.FILES['FU_img']
        data.product_name = request.POST.get('TBX_pname')
        data.product_type = request.POST.get('TBX_ptype')
        data.descr = request.POST.get('TBX_desc')
        data.price = request.POST.get('TBX_price')
        data.save()
    
    return render(request, 'editproduct.html', context)

