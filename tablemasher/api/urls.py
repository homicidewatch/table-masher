from django.conf.urls.defaults import *
from piston.resource import Resource

from api.handlers import TableHandler, ColumnHandler
table_resource = Resource(TableHandler)
column_resource = Resource(ColumnHandler)

urlpatterns = patterns('',
    url(r'^tables/?$', table_resource),
    url(r'^tables/(?P<id>\d+)/?$', table_resource),
    url(r'^tables/(?P<id>\d+)/columns/?$', column_resource),
)