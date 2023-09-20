from django.contrib import admin
from .models import Qualifications,Branches,Years,Sems
class Qualifications_Display(admin.ModelAdmin):
    class Meta:
        list_display=['name']

class Branches_Display(admin.ModelAdmin):
    class Meta:
        list_display=['name']
class Years_Display(admin.ModelAdmin):
    class Meta:
        list_display=['name']
class Sems_Display(admin.ModelAdmin):
    class Meta:
        list_display=['name']


admin.site.register(Qualifications,Qualifications_Display)
admin.site.register(Branches,Branches_Display)
admin.site.register(Years,Years_Display)
admin.site.register(Sems,Sems_Display)

# Register your models here.
