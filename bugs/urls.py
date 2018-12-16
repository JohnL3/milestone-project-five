from django.conf.urls import url
from bugs.views import get_bugs, bug_details, upvote, bug_issue


urlpatterns = [
    url(r'^$', get_bugs, name='bugs'),
    url(r'^(?P<pk>\d+)/$', bug_details, name='bug_details'),
    url(r'^upvote/$', upvote, name='upvote'),
    url(r'^issue/$', bug_issue, name='issue'),
]