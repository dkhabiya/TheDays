from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'signUp/$', views.signUp, name='signUp'),
    url(r'getLogin/$', views.getLogin, name='getLogin'),
    url(r'/login/', views.doLogin, name='doLogin'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'landing'}, name='logout'),
    url(r'user$', views.activityList, name='activityList'),
    url(r'^update/(?P<pk>\d+)/$', views.update, name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]