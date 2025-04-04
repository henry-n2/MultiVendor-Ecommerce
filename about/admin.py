from django.contrib import admin
from products.admin import super_admin_site

from .models import AboutUs, TeamMember

# Register existing models

# Customize AboutUs model in admin
@admin.register(AboutUs, site=super_admin_site)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'experience_years', 'award_title')
    search_fields = ('title', 'subtitle', 'description')
    list_filter = ('experience_years',)
    ordering = ('title',)


# Customize TeamMember model in admin
@admin.register(TeamMember, site=super_admin_site)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')
    ordering = ('name',)
