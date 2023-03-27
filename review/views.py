from django.shortcuts import render, HttpResponseRedirect
from .forms import BuildingAdd 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
 
def django_from(request): 
    frm = BuildingAdd(request.POST)
    if request.method=='POST':
        if frm.is_valid():
            frm.save()
        else:
            frm=BuildingAdd
    return render(request,'review/review.html', {'form':frm})


#login form

def login_form(request):
    frm = AuthenticationForm()
    if request.method=="POST":
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data['username']
            userp = frm.cleaned_data['password']
            user = authenticate(username = usern,password = userp)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('review/success.html')
            else:
                frm = AuthenticationForm()
                return render(request, 'review/login.html',{'form': frm})
    #frm = AuthenticationForm()
    return render(request,'review/login.html',{'form':frm})

def login_success(request):
    render(request, 'review/success.html')