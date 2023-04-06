from .models import MySiteUser,CreateProgrammingLanguage;
from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

class UserProgrammingLanguage(admin.ModelAdmin):
    list_display = ("name", "count")

admin.site.register(MySiteUser, UserAdmin)
admin.site.register(CreateProgrammingLanguage, UserProgrammingLanguage)
