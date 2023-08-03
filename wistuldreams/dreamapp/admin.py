from django.contrib import admin

# Register your models here.
from .models import Tag, Dream

admin.site.register(Tag)
admin.site.register(Dream)
