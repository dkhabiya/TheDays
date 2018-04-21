from django.shortcuts import render
from django.utils import timezone
from .models import Activity

# Create your views here.
def activityList(request):
    activities = Activity.objects.filter(dateCreated__lte=timezone.now()).order_by('dateCreated')
    return render(request, 'app/activityList.html', {'activities': activities})