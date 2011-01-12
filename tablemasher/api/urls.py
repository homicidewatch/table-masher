from django.conf.urls.defaults import *
from piston.resource import Resource

from api.handlers import TableHandler
table_resource = Resource(TableHandler)

urlpatterns = patterns('',
    url(r'^tables/?', table_resource),
    url(r'^tables/(?P<id>\d+)/?', table_resource),
)