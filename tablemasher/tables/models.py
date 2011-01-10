import datetime
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from tables.fields import SeparatedValuesField
from tables.storage import OverwritingStorage
from table_fu import TableFu
from taggit.managers import TaggableManager

class Table(models.Model):
    """
    A table imported into TableMasher, possibly by
    way of TableFu. Top-level attributes are editorial
    metadata. Data points to a CSV stored in the filesystem.
    """
    added_by = models.ForeignKey(User, related_name='tables')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    tags = TaggableManager()
    
    # actual data
    columns = SeparatedValuesField(blank=True, null=True)
    url = models.URLField(blank=True)
    file = models.FileField(blank=True, upload_to='tables/%Y/%m/%d', storage=OverwritingStorage())
    
    class Meta:
        get_latest_by = "updated"
        ordering = ('-updated',)
    
    def  __unicode__(self):
        return self.title
    
    @property
    def data(self):
        """Return a TableFu instance with data for this model"""
        if hasattr(self, '_data') and self._data is not None:
            return self._data
        
        if self.file:
            # this gets wrapped in a with block for cleanliness
            d = TableFu.from_file(os.path.join(settings.MEDIA_ROOT, self.file.name))
        
        elif self.url:
            d = TableFu.from_url(self.url)
        
        if self.columns:
            d.columns = self.columns
        
        self._data = d
        return self._data
    
