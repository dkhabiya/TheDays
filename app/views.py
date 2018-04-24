from django.shortcuts import render
from django.shortcuts import redirect
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

# Get activity list.
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
    
    if request.method == "POST" and 'done' in request.POST:
        print('Done')
        form = ActivityForm(request.POST)
        print(request.POST.get('id'))
        # if form.is_valid():
        #     activity = form.save(commit=False)
        #     activity.user = request.user
        #     activity.dateCreated = timezone.now()
        #     activity.save()
        return redirect('activityList')
    
    return render(request, 'app/activityList.html', {'activities': activities})

# @login_required
# def activityNew(request):
#     if request.method == "POST":
#         print("Here")
#         form = ActivityForm(request.POST)
#         print(form)
#         if form.is_valid():
#             activity = form.save(commit=False)
#             activity.user = request.user
#             activity.dateCreated = timezone.now()
#             activity.save()
#             return redirect('activityList')
#     else:
#         form = ActivityForm()
#     return render(request, 'app/activityNew.html', {'form': form})

