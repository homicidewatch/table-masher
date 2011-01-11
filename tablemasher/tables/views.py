from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from tables.models import Table

def table_detail(request, id):
    table = get_object_or_404(Table.objects.public(), id=id)
    return render_to_response('tables/table_detail.html', {
                              'table': table
                              }, RequestContext(request))