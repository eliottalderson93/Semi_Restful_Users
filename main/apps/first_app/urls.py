from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index), #template
    url(r'^users$', views.index), #template
    url(r'^users/(?P<id>\d+)/update$', views.update), #post #updates the DB and redirects to users
    url(r'^users/add$', views.create), #post
    url(r'^users/new$', views.new), #template
    url(r'^users/(?P<id>\d+)$', views.show), #template
    url(r'^users/(?P<id>\d+)/edit$', views.edit), #template
    url(r'^users/(?P<id>\d+)/delete$', views.destroy) #post
]
