import os
from django.core.files import File
from django.contrib.auth.models import User
from django.test import TestCase
from tables.models import Table
from table_fu import TableFu

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

class TableTest(TestCase):
    
    def setUp(self):
        self.filename = os.path.join(DATA_DIR, 'arra.csv')
        self.file = open(self.filename)
        self.user = User.objects.create_user('Joe', 'plumber@example.com', 'password')
    
    def tearDown(self):
        self.file.close()

class DataTest(TableTest):
    
    def test_from_file(self):
        arra = TableFu.from_file(self.filename)
        tabled = Table(
            title = "That Stimulus",
            added_by = self.user,
            file = File(self.file)
        )
        
        self.assertEqual(arra.table, tabled.data.table)