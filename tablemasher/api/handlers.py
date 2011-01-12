from piston.handler import BaseHandler
from piston.utils import rc, throttle

from tables.models import Table

class TableHandler(BaseHandler):
    """
    Fetch table info
    """
    allowed_methods = ('GET',)
    model = Table
    
    def read(self, request, **kwargs):
        if 'id' in kwargs:
            try:
                table = Table.objects.get(pk=kwargs['id'])
                return table
            except Table.DoesNotExist:
                return rc.NOT_FOUND
    

class ColumnHandler(BaseHandler):
    """
    Get or set columns for a table
    """
    pass