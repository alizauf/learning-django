from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name']}),
		('Interaction Information', {'fields': ['likes', 'views', 'slug']}),
		]
	list_display = ('name', 'likes', 'views', 'slug')

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'category', 'url', 'views']	
	list_display = ('title', 'category', 'url', 'views')

admin.site.register(Page, PageAdmin)
	


#simple version
#admin.site.register(Category)
#admin.site.register(Page)
