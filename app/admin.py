from django.contrib import admin

from app.models import User, Category, Item

# Register your models here.

admin.site.register([
    User,
    Category,
    Item
])
