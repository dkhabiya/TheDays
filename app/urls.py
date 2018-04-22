from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.activityList, name='activityList'),
    url(r'^activity/new/$', views.activityNew, name='activityNew'),
]