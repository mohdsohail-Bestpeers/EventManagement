from django.shortcuts import render
from .models import EventUser, Event, Address, event_photo
from .forms import event_user_form, event_form, address_form, event_photo_form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def result(request):
    d = Event.objects.all()
    form1 = event_form()
    form2 = address_form()
    form3 = event_photo_form()
    if request.method == "POST":
        form1 = event_form(request.POST)
        form2 = address_form(request.POST)
        form3 = event_photo_form(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            events = form1.save()

            form2.save(commit=False)
            form2.instance.event = events
            form2.save()

            form3.save(commit=False)
            form3.instance.event = events
            form3.save()
            form1 = event_form()
            form2 = address_form()
            form3 = event_photo_form()
    context = {"form1": form1, "form2": form2, "form3": form3, "data": d}
    return render(request, "result.html", context)

'''Mobile number validation'''  
# def user(request):
#     form = user_form()
#     if request.method == "POST":
#         form = user_form(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, "user.html", {"form": form})

def detail(request, x):
    if request.user.is_authenticated:
        objs = Event.objects.filter(publisher__first_name=x)
        return render(request, 'result.html', {'objs':objs})
    else:
        return HttpResponseRedirect('/login/')

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user != None:
                    login(request, user)
                    return HttpResponseRedirect('/'+user.first_name+'/detail/')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/'+request.user.first_name+'/detail/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')