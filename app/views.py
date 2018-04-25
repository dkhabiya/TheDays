from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import ActivityForm, SignUpForm
from .models import Activity

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
            login(request, user)
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'app/signUp.html', {'form': form})

# Get activity list based on user login.
@login_required    
def activityList(request):
    activities = Activity.objects.filter(user=request.user).order_by('dateCreated')
    
    if request.method == "POST" and 'add' in request.POST:
        print('Add')
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.dateCreated = timezone.now()
            activity.save()
            return redirect('activityList')
    
    return render(request, 'app/index.html', {'activities': activities})

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
      
  