from django.contrib import admin

from .models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ('id', 'title')
