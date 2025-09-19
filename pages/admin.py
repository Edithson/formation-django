from django.contrib import admin
from .models import ContactMessage
# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_treated')
    list_filter = ('is_treated', 'created_at',)
    search_fields = ('name', 'email')

admin.site.register(ContactMessage, ContactMessageAdmin)