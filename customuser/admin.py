from django.contrib import admin

#Register your models here.
from .models import MyUser


class UserAdmin(admin.ModelAdmin):
    list_display=['username','user_type']
    list_filter = ['user_type']

admin.site.register(MyUser, UserAdmin)
