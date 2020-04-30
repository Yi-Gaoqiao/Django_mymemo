from django.contrib import admin
from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')

admin.site.register(Memo, MemoAdmin)