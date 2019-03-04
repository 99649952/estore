from django.contrib import admin
from .models import User
from .models import UserInfo


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'user_info')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'qq', 'mobile')


admin.site.register(User, UserAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
