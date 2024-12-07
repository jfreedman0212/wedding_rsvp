from django.contrib import admin

from .models import GuestGroupEmailInvitation, GuestGroup, Guest


class GuestInline(admin.StackedInline):
    model = Guest
    extra = 3
    min_num = 1
    fields = ['name']


class GuestGroupAdmin(admin.ModelAdmin):
    fields = ['name', 'email']
    inlines = [GuestInline]
    search_fields = ['name', 'guests__name']
    list_display = ['name', 'status', 'updated_at']
    list_filter = ['updated_at', 'status']


class GuestAdmin(admin.ModelAdmin):
    search_fields = ['name', 'group__name']
    list_filter = ['status']
    list_display = ['name', 'group__name', 'status', 'has_dietary_restriction']


class GuestGroupEmailInvitationAdmin(admin.ModelAdmin):
    fields = ['group', 'expires_at']
    list_filter = ['slug', 'group__name']
    list_display = ['group__name', 'slug', 'expires_at']
    list_filter = ['expires_at']


admin.site.register(Guest, GuestAdmin)
admin.site.register(GuestGroup, GuestGroupAdmin)
admin.site.register(GuestGroupEmailInvitation, GuestGroupEmailInvitationAdmin)
