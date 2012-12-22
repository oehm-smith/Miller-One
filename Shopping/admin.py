from django.contrib import admin

from Shopping.models import Item
from Shopping.models import Store

class ItemsAdmin(admin.ModelAdmin):
    fieldsets = [('Details', {'fields':['name','brand','cost','datebought','store']})]
    list_display = ('id','name','brand','cost','datebought','store')
    list_display_links = ('id','cost','datebought')
    list_editable = ('name','brand')
    list_filter = ['datebought','name','brand','store']
    date_hierarchy = 'datebought'
    search_fields = ['name','brand','cost']
    list_per_page = 20
    
admin.site.register(Item,ItemsAdmin)
admin.site.register(Store)
