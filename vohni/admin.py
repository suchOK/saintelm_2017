from django.contrib import admin
from .models import Journey, User_Email, Day, CoverImage
# Register your models here.


class JourneyAdmin(admin.ModelAdmin):
  list_display = ('title', 'cities')
  filter_horizontal = ('day',)


class DayAdmin(admin.ModelAdmin):
  list_display = ('title_day', 'description')


class User_EmailAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'get_journey_choice')

  def get_journey_choice(self, obj):
    return obj.journey_choice.title

   

admin.site.register(Journey, JourneyAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(User_Email, User_EmailAdmin)
admin.site.register(CoverImage)
