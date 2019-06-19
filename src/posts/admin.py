from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["tittle", "update", "timestamp"]
    list_display_links = ["update"]
    list_editable = ["tittle"]
    list_filter = ["update","timestamp"]
    search_fields = ["tittle", "content"]
    
    class Meta:
        model: Post 

admin.site.register(Post,PostModelAdmin)