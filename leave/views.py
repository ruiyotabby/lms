from django.shortcuts import render, redirect
# Create your views here.
from .forms import *
from django.contrib import messages

def homePage(request):
    return render(request, 'leave/home.html')

def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.clean_pjnumber():
            # pjnumber = form.cleaned_data.get('pjnumber')
            messages.succes(request, f'Account created for {pjnumber}!')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form':form}
    return render(request, 'leave/register.html', context)

def loginPage(request):
    return render(request, 'leave/login.html')