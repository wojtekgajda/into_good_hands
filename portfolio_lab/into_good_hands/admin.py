from django.contrib import admin

from .models import CustomUser, Institution, Category
admin.site.register(CustomUser)
admin.site.register(Institution)
admin.site.register(Category)




