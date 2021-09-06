from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)

    # Fieldset controls what fields are shown when altering or viewing a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Dates', {'fields': ('date_joined', 'last_login')}),
    )

    # Add_fieldsets controls what fields are shown when adding a new user
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    readonly_fields = ('date_joined', 'last_login')

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
