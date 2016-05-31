from django.conf.urls import url

from . import views

app_name = 'notifications'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^message/$', views.message, name='message'),
    url(r'^auth/$', views.auth, name='auth'),

]