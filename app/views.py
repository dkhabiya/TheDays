from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (login as auth_login, authenticate)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import ActivityForm, SignUpForm
from .models import Activity

import itertools
import functools
import re

# Landing.
def landing(request):
    return render(request, 'app/landing.html')
    
# Sign up.
def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'app/signUp.html', {'form': form})
    
# Login page load.    
def getLogin(request):
    return render(request, 'app/getLogin.html')

# Do login 
def doLogin(request):
    _message = ''
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password1']
        
        if User.objects.filter(username=_username).exists():
            user = authenticate(username=_username, password=_password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/user')
                else:
                    _message = '* Your account is not activated.'
            else:
                _message = '* Incorrect Password.'
        else:
            _message = '* User does not exist.'
            
    context = {'message': _message}
    return render(request, 'app/getLogin.html', context)
    
# Get activity list based on user login.
@login_required    
def activityList(request):
    activities = Activity.objects.filter(user=request.user).order_by('dateCreated')
    
    if request.method == "POST" and 'add' in request.POST:
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.dateCreated = timezone.now()
            activity.save()
            return redirect('activityList')
    
    return render(request, 'app/index.html', {'activities': activities, 'counter': functools.partial(next, itertools.count(1))})

# Update status of activity.
@login_required
def update(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    
    if(activity.done) :
        activity.done = False
    else:
        activity.done = True
    activity.dateCreated = timezone.now()    
    activity.save()
    
    return redirect('activityList')
    
# Delete activity.
@login_required
def delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    activity.delete()
    
    return redirect('activityList')
    
def validate(value):
    error=''
    while True:
        if len(value) < 5:
            error="* Password too short."
        elif re.search('[0-9]',value) is None:
            error="Make sure your password has a number in it"
            break
        elif re.search('[A-Z]',value) is None: 
            error="Make sure your password has a capital letter in it"
            break
        
    return error
               