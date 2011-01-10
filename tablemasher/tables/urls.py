from django.conf.urls.defaults import *
from django.views.generic import list_detail

from tables.models import Table

urlpatterns = patterns('tables.views',
    url(r'^$', 
        list_detail.object_list, 
        {'queryset': Table.objects.public()},
        name='tables_table_list'),
)