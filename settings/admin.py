from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Setting,Delivery_fee

class SettingAdmin(SummernoteModelAdmin):
    list_display=['name','call_us','phones']
    search_fields=['name','subtitle']
    #list_filter=[]
    summernote_fields = ('subtitle',)

admin.site.register(Setting,SettingAdmin)
admin.site.register(Delivery_fee)
