from django.contrib import admin

# Register your models here.
from .models import Contact,Member

admin.site.register(Contact)
admin.site.register(Member)
