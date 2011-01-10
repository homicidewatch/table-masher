from django.contrib import admin
from tables.models import Table

class TableAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(Table, TableAdmin)
