from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Admin)
admin.site.register(UserType)

admin.site.register(User)
admin.site.register(Assignment)
admin.site.register(Result)
admin.site.register(Leave)