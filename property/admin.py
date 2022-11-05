from django.contrib import admin

from .models import Complaint, Flat, Owner

class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']
    list_display = ['address', 'price', 'new_building', 'construction_year']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'floor', 'rooms_number', 'has_balcony', 'active']
    raw_id_fields = ['liked_by']
    inlines = [OwnersInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = ['full_name', 'phonenumber', 'pure_phone']
    search_fields = ['full_name', 'pure_phone']
