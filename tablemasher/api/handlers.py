from piston.handler import BaseHandler
from piston.utils import rc, throttle

from tables.models import Table

class TableHandler(BaseHandler):
    """
    Fetch table info
    """
    allowed_methods = ('GET',)
    model = Table
    exclude = ('added_by',)
    
    def read(self, request, **kwargs):
        if 'id' in kwargs:
            try:
                table = Table.objects.public().get(pk=kwargs['id'])
                return table
            except Table.DoesNotExist:
                return rc.NOT_FOUND
        
        else:
            return Table.objects.public()
    

class ColumnHandler(BaseHandler):
    """
    Get or set columns for a table
    """
    
    def read(self, request, id, **kwargs):
        try:
            table = Table.objects.public().get(pk=id)
        except Table.DoesNotExist:
            return rc.DOES_NOT_EXIST
        
        return table.columns
    
    def update(self, request, id, **kwargs):
        try:
            table = Table.objects.public().get(pk=id)
        except Table.DoesNotExist:
            return rc.DOES_NOT_EXIST
        
        table.columns = request.data.get('columns', None)
        table.save()
        return table.columns

class DataHandler(BaseHandler):
    
    def read(self, request, id, **kwargs):
        try:
            table = Table.objects.public().get(pk=id)
        except Table.DoesNotExist:
            return rc.DOES_NOT_EXIST
        
        return list(table.data.dict())
    