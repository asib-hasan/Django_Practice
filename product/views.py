from django.shortcuts import render
from product.forms import RecentProduct
from django.http import HttpResponseRedirect
from .models import Laptop
# Create your views here.

def send(request):
    return render(request,'product/submit.html')

def details(request):
    if request.method == 'POST':
        frm = RecentProduct(request.POST)
             
        if frm.is_valid():
            pas = frm.cleaned_data['password']
            rpas = frm.cleaned_data['re_password']
            lap = frm.cleaned_data['laptop']
            eml = frm.cleaned_data['email']
            rm = frm.cleaned_data['ram']
            you = frm.cleaned_data['youtube']
            buy = Laptop(password=pas,laptop=lap, email=eml, ram=rm, youtube = you,
                         re_password = rpas)
            buy.save()
            return HttpResponseRedirect('/product/successfully')
            
    else:
        frm = RecentProduct()
        
    return render(request, 'product/recent.html',{'form':frm})

