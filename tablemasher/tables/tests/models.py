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
        self.url = "https://spreadsheets.google.com/pub?key=0Aj9jJP3NwZQAdFlkTGtOYnhuNE9ZcHpIY1pHcDlnQUE&hl=en&single=true&gid=1&output=csv"
    
    def tearDown(self):
        self.file.close()

class DataTest(TableTest):
    
    def test_from_url(self):
        murders = TableFu.from_url(self.url)
        tabled = Table(
            title = "DC Homicides 2010",
            added_by = self.user,
            url = self.url
        )
        tabled.save()
        
        self.assertEqual(murders.table, tabled.data.table)
    
    def test_from_file(self):
        arra = TableFu.from_file(self.filename)
        tabled = Table(
            title = "That Stimulus",
            added_by = self.user,
            file = File(self.file),
        )
        tabled.save()
        
        self.assertEqual(arra.table, tabled.data.table)
    
    def test_set_columns(self):
        arra = TableFu.from_file(self.filename)
        arra.columns = ["State", "County", "Urban Area"]
        
        tabled = Table(
            title = "That Stimulus",
            added_by = self.user,
            file = File(self.file),
            columns = ["State", "County", "Urban Area"]
        )
        tabled.save()
        
        self.assertEqual(arra.columns, tabled.data.columns)
    
    def test_no_data(self):
        nada = Table.objects.create(title="Nothing to see here", added_by=self.user)
        self.failIf(nada.data)
