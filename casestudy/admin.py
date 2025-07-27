from django.contrib import admin
from .models import Client, Location, Industry, Casestudy, Comment

# Register your models here.
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Industry)
admin.site.register(Casestudy)
admin.site.register(Comment)