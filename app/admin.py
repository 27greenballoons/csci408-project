from django.contrib import admin

from .models import ContactMessage, Location

# Register your models here. These are the same thing except they'll show up in the admin panel.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'owner') # show what fields can be seen in admin panel
    search_fields = ('city', 'state', 'owner') # search by these fields 
    list_filter = ('city', 'state') # filter by this field 