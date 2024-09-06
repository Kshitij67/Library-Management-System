from django.contrib import admin
from .models import book, Users

admin.site.register(book)
admin.site.register(Users)