from django.contrib import admin
from .models import Xabar
# Register your models here.

class XabarAdmin(admin.ModelAdmin):
    list_display = ['mavzu', 'holati', 'yangilangan_vaqti']
    list_filter = ['holati', 'mavzu']
    search_fields = ['mavzu', 'matn']
    prepopulated_fields = {'link_matn': ('mavzu',)}
    raw_id_fields = ('muallif',)
    date_hierarchy = 'elon_vaqti'


admin.site.register(Xabar, XabarAdmin)