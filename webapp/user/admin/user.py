from django.contrib import admin
from django.core.files import File
from user.models import User, get_random_profile_filename


def reset_avatar(self, request, querset):
    for user in querset:
        filename = get_random_profile_filename()
        f = open("staticfiles/" + filename, "rb")
        user.avatar = File(f)
        user.save()
        f.close()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin View for User"""

    actions = [reset_avatar]

    list_display = (
        "email",
        "username",
    )
