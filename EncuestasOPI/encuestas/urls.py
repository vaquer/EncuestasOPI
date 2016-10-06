from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.view_polls, name='polls_view'),
    url(r'^view/(?P<slug>[-_a-zA-Z0-9]+)/$', views.view_poll, name='single_view'),
    url(r'^json/$', views.view_json_polls, name='view_json'),

]