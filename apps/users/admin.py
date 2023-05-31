from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from apps.users.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if bool(self.cleaned_data['email']):
            user.email = self.cleaned_data['email'];
        else:
            user.email = None;
        if 'password' in self.changed_data:
            user.set_password(self.cleaned_data["password"]);
        if commit:
            user.save()
        return user


fieldsets = (
        (None, {'fields': (
            'uniqueId',
            'logo',
            'email',
            'name',
            'surname',
            'phone_one',
            'dob',
            'card',
            'password',
            'resetPasswordUUID',
            'resetPasswordDate',
        )}),
        )


class CustomUserAdmin(UserAdmin):
    search_fields = ['email'];
    add_form = UserCreationForm
    form = UserCreationForm
    list_display = ['uniqueId', 'email']
    list_display_links = ['email', 'uniqueId']
    ordering = ("-id",)

    fieldsets = fieldsets

    add_fieldsets = fieldsets

admin.site.register(User, CustomUserAdmin);
admin.site.unregister(Group);