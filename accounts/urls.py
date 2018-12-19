from django.conf.urls import url, include
from accounts.views import index, logout, login, register, register_login, profile

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^$', index, name='home'),
    url(r'^register_login/$', register_login, name='register_login'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
]