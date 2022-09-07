from django.contrib import admin

from .models import Team, UserProfile

admin.site.register(Team)
admin.site.register(UserProfile)