from django.conf.urls.defaults import *
from django.views.generic import list_detail

from tables.models import Table

urlpatterns = patterns('tables.views',
    url(r'^$', 
        list_detail.object_list, 
        {'queryset': Table.objects.public().select_related('added_by')},
        name='tables_table_list'),
    
    url(r'^(?P<id>\d+)/$', 'table_detail', name='tables_table_detail'),
)