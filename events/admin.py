from django.contrib import admin
from .models import Event, Entry
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('name','slug','status','date')
    search_fields = ['name', 'excerpt']
    list_filter = ('status', 'date')
    prepopulated_fields ={'slug': ('name',)}
    summernote_fields = ('excerpt')


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'nick_name', 'clan', 'event','created_on', 'approved',)
    list_filter = ('approved', 'created_on')
    search_fields = ['event', 'nick_name', 'email', 'clan']
    actions = ['approve_entries']

    def approve_entries(self, request, queryset):
        queryset.update(approved=True)
