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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('casestudy', 'author', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'content', 'casestudy__title')
    list_editable = ('approved',)
    actions = ['approve_comments', 'disapprove_comments']
    
    def content_preview(self, obj):
        """Show first 50 characters of comment content"""
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Comment Preview'
    
    def approve_comments(self, request, queryset):
        """Bulk action to approve selected comments"""
        updated = queryset.update(approved=True)
        if updated == 1:
            message = '1 comment was successfully approved and is now visible to users.'
        else:
            message = f'{updated} comments were successfully approved and are now visible to users.'
        self.message_user(request, message, level='SUCCESS')
    approve_comments.short_description = "✓ Approve selected comments"
    
    def disapprove_comments(self, request, queryset):
        """Bulk action to disapprove selected comments"""
        updated = queryset.update(approved=False)
        if updated == 1:
            message = '1 comment was disapproved and is now hidden from public view.'
        else:
            message = f'{updated} comments were disapproved and are now hidden from public view.'
        self.message_user(request, message, level='WARNING')
    disapprove_comments.short_description = "✗ Disapprove selected comments"

# Register your models here.
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Industry)
# Comment is now registered with @admin.register decorator above