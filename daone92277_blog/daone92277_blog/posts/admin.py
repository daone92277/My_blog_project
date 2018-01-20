from django.contrib import admin
from .models import Post


#remove the default "itemobject" text from django admin
class UserPost(admin.ModelAdmin):
    list_display = ["title", "pub_date", "image", "body"]


    
# Register your models here.
admin.site.register(Post, UserPost)

