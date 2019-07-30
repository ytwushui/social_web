from django.contrib import admin

from . import models

# enable to edit models in the same page as the parent model
#TabularInline class
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
