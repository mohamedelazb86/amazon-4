from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Setting

class SettingAdmin(SummernoteModelAdmin):
    list_display=['name','call_us','phones']
    search_fields=['name','subtitle']
    #list_filter=[]
    summernote_fields = ('subtitle',)

admin.site.register(Setting,SettingAdmin)
