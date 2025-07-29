from django.contrib import admin
from .models import Client, Location, Industry, Casestudy, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Casestudy)
class CasestudyAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug',)
    search_fields = ['title']
    #list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

# Register your models here.
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Industry)
admin.site.register(Comment)