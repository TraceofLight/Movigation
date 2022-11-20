from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


class SMSAuthAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
