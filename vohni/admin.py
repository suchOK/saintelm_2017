from django.contrib import admin
from .models import Journey, User_Email, Day
# Register your models here.

admin.site.register(Journey)
admin.site.register(Day)
admin.site.register(User_Email)
