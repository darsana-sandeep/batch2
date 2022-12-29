from django.contrib import admin

# Register your models here.
from batch2.models import ProfileData, Member

admin.site.register(ProfileData)
admin.site.register(Member)