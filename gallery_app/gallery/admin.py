from django.contrib import admin
from gallery.models import Picture



class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'description', 'created_at', 'author')
    list_filter = ('id', 'picture', 'description', 'created_at', 'author')
    search_fields = ('picture', 'description', 'created_at', 'author')
    fields = ('picture', 'description', 'created_at', 'author')
    readonly_fields = ('id', 'created_at', 'author')


admin.site.register(Picture, PictureAdmin)