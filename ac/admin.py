from django.contrib import admin
from ac.models import AakashCentre, Coordinator
from ac.models import Project, TeamMember, Mentor
from ac.models import Contact, Faq, Pub


class ProjectAdmin(admin.ModelAdmin):
    """Modify admin's Project page."""
    list_display = ('name', 'ac', 'approve')
    search_fields = ('name',)


class AcAdmin(admin.ModelAdmin):
    """Aakash Centre admin page."""
    list_display = ('ac_id', 'name', 'coordinator', 'city', 'state')
    search_fields = ('ac_id',)


class CoordinatorAdmin(admin.ModelAdmin):
    """Coordinator page."""
    list_display = ('user', 'contact')
    search_fields = ('user__username',) # user__fieldname, else it
                                        # throws error: Related Field
                                        # has invalid lookup:
                                        # icontains


admin.site.register(AakashCentre, AcAdmin)
admin.site.register(Coordinator, CoordinatorAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(TeamMember)
admin.site.register(Mentor)

admin.site.register(Contact)
admin.site.register(Faq)
admin.site.register(Pub)

