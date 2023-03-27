from django.contrib import admin
from .models import Laptop
# Register your models here.

#admin.site.register(Laptop)
@admin.register(Laptop)
class laptopAdmin(admin.ModelAdmin):
    list_display = ('password','re_password','laptop','email','ram','youtube')