from django.contrib import admin

from .models import Complaint, Flat, Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'floor', 'rooms_number', 'has_balcony', 'active']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = ['owner', 'owners_phonenumber', 'owner_pure_phone']
    search_fields = ['owner', 'owner_pure_phone']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
