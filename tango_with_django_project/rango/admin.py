from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name']}),
		('Interaction Information', {'fields': ['likes', 'views']}),
		]
	list_display = ('name', 'likes', 'views')

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'category', 'url', 'views']	
	list_display = ('title', 'category', 'url', 'views')

admin.site.register(Page, PageAdmin)
	


#simple version
#admin.site.register(Category)
#admin.site.register(Page)
