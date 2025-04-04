from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from accounts.forms import RegistrationForm
from products.admin import super_admin_site


# class CustomUserAdmin(UserAdmin):

#     class Meta(UserChangeForm.Meta):
#         model = CustomUser

#     form = RegistrationForm
#     list_display = ('email', 'id', 'first_name', 'last_name', 'mobile','user_role','is_active', 'is_staff', 'is_superuser')

#     fieldsets = (
#         # (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name','profile_picture', 'trade_license_number', 'gst_number' , 'email' , 'mobile')}),
#         ('Permissions', {'fields': ( 'user_role','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#     )
    
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'mobile')}),
#         ('Permissions', {'fields': ('user_role','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#     )
#     ordering = ('email',)
#     search_fields = ("first_name", "last_name", "email")

# super_admin_site.register(CustomUser, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):

    class Meta(UserChangeForm.Meta):
        model = CustomUser

    form = RegistrationForm
    list_display = ('email', 'id', 'first_name', 'last_name', 'mobile','user_role','is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'last_name', 'profile_picture', 'trade_license_number', 'gst_number', 'email', 'mobile')}),
        ('Permissions', {'fields': ('user_role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'mobile')}),
        ('Permissions', {'fields': ('user_role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    ordering = ('email',)
    search_fields = ("first_name", "last_name", "email")
    
def has_module_permission(self, request):
    if request.user.is_authenticated and (request.user.is_superuser or getattr(request.user, 'user_role', None) == '2'):
        return True
    return super().has_module_permission(request)
    
def has_view_permission(self, request, obj=None):
    if request.user.is_authenticated and (request.user.is_superuser or getattr(request.user, 'user_role', None) == '2'):
        return True
    return super().has_view_permission(request, obj)
    
def has_add_permission(self, request, obj=None):
    if request.user.is_authenticated and (request.user.is_superuser or getattr(request.user, 'user_role', None) == '2'):
        return True
    return super().has_add_permission(request, obj)
    
def has_change_permission(self, request, obj=None):
    if request.user.is_authenticated and (request.user.is_superuser or getattr(request.user, 'user_role', None) == '2'):
        return True
    return super().has_change_permission(request, obj)
    
def has_delete_permission(self, request, obj=None):
    if request.user.is_authenticated and (request.user.is_superuser or getattr(request.user, 'user_role', None) == '2'):
        return True
    return super().has_delete_permission(request, obj)


super_admin_site.register(CustomUser, CustomUserAdmin)

