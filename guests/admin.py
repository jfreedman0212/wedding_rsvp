from django.contrib import admin

from .models import GuestGroup, Guest


class GuestInline(admin.StackedInline):
    model = Guest
    extra = 3
    min_num = 1
    fields = ['name']


class GuestGroupAdmin(admin.ModelAdmin):
    fields = ['email']
    inlines = [GuestInline]


admin.site.register(Guest)
admin.site.register(GuestGroup, GuestGroupAdmin)
