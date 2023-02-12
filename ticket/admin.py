from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from blog.models import Post
from .models import Ticket, Replie

# Register your models here.
class ProjectAdmin(GuardedModelAdmin):
	pass
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Ticket, ProjectAdmin)
admin.site.register(Replie, ProjectAdmin)
