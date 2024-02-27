from django.contrib import admin
from . models import Category,Types
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)


class TypesAdmin(admin.ModelAdmin):
    
    prepopulated_fields={'slug':('name',)}
    
    
admin.site.register(Types,TypesAdmin)

