from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'signUp/$', views.signUp, name='signUp'),
    url(r'login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'landing'}, name='logout'),
    url(r'user$', views.activityList, name='activityList'),
    # url(r'^activity/new/$', views.activityNew, name='activityNew'),
]