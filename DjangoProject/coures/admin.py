from django.contrib import admin
from .models import Category,Course
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Course)
# Register your models here.
