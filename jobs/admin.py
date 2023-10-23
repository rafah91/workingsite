from django.contrib import admin
from .models import Job, Company , Category

class JobAdmin(admin.ModelAdmin):
    list_display=['title','category','agency','salary','location']
    list_filter=['nature','category']
    search_fields=['title','nature','salary']
    



# Register your models here.
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Category)
