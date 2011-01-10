import datetime
from mongoengine import *

class Table(Document):
    """
    A table imported into TableMasher, possibly by
    way of TableFu. Top-level attributes are editorial
    metadata. Rows are a list of dictionary fields.
    """
    title = StringField()
    description = StringField()
    created = DateTimeField(default=datetime.datetime.now)
    updated = DateTimeField(default=datetime.datetime.now)
    public = BooleanField(default=True)
    
    columns = ListField(StringField())
    rows = ListField(DictField())