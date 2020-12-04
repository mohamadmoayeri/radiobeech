from django.contrib import admin

# Register your models here.

from .models import story

class STORY(admin.ModelAdmin):
      fieldsets=[(None,{'fields':('user','title')}),
      ("available",{'fields':("sound","image","caption")})]
      list_display=['title','sound']
      search_fields=['title']
      list_per_page=10
      #list_display_links=['sound']
     # list_editable=['title']
      list_filter=['user']
      list_max_show_all=3
      #date_hierarchy='date'
      #filter_vertical=('many',)
      #ordering=('-date',)
      #raw_id_fields=('many',)
admin.site.register(story,STORY)
