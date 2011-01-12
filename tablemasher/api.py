from tastypie.resources import ModelResource
from tastypie.api import Api

v1 = Api(api_name='v1')

from tables.models import Table

class TableResource(ModelResource):
    
    class Meta:
        queryset = Table.objects.public()


v1.register(TableResource())