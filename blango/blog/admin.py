from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) # it allows our model create table and db appear in the admin interface