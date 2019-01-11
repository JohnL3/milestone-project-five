from django.conf.urls import url
from .views import get_features, single_feature, feature_form

urlpatterns = [
    url(r'^$', get_features, name='features'),
    url(r'^(?P<pk>\d+)/$', single_feature, name='single_feature'),
    url(r'^details/$', feature_form, name='details'),
]