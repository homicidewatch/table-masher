from django.core.urlresolvers import reverse
from django.test import TestCase

from tables.models import Table


class ViewTest(TestCase):
    
    fixtures = ['tables.json']
    
    def test_table_detail(self):
        t1 = Table.objects.get(pk=1)
        
        resp = self.client.get(reverse('tables_table_detail', args=[t1.id]))
        self.assertEqual(resp.status_code, 200)
        
        t2 = resp.context['table']
        
        self.assertEqual(t1.data.table, t2.data.table)
