from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .forms import ActivityForm
from .models import Activity

# Create your views here.
def activityList(request):
    activities = Activity.objects.filter(dateCreated__lte=timezone.now()).order_by('dateCreated')
    return render(request, 'app/activityList.html', {'activities': activities})

def activityNew(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.dateCreated = timezone.now()
            activity.save()
            return redirect('activityList')
    else:
        form = ActivityForm()
    return render(request, 'app/activityNew.html', {'form': form})
