from django.contrib import admin
from core.models import User, Sales, Rating, Restaurant

# Register your models here.
admin.site.register(Sales)
admin.site.register(Rating)
admin.site.register(Restaurant)
