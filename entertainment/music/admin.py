from django.contrib import admin

from . models import Artist, Album, Song

class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register (Artist, SiteAdmin)
admin.site.register (Album, SiteAdmin)
admin.site.register (Song)
