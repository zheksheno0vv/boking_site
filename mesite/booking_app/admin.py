from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin



class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 1

class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelPhotoInline]


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotoInline]



@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelPhotoInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomPhotoInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Country)
admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Booking)