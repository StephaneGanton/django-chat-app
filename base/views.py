from django.shortcuts import render, redirect
from  django.contrib.auth import login

from .forms import SignUpForm

def frontpageView(request):

    return render(request, 'base/frontpage.html')

def signupView(request):

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')

    else:
        form = SignUpForm()
    
    return render(request, 'base/signup.html', {'form': form})