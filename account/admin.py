from django.contrib import admin
from unfold.admin import ModelAdmin

from account.models.users import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass
