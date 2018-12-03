from django.conf.urls import url
from blog.views import get_posts, single_post, create_edit_post

urlpatterns = [
     url(r'^posts/$', get_posts, name='get_posts'),
     url(r'^posts/new/$', create_edit_post, name='new_post'),
     url(r'^posts/(?P<pk>\d+)/$', single_post, name='single_post'),
     url(r'^(?P<pk>\d+)/edit/$', create_edit_post, name='edit_post'),
]