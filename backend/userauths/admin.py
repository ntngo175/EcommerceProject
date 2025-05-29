from django.contrib import admin
#2025/05/29 NhonNT17 added start.
from userauths.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)
#2025/05/29 NhonNT17 added end.
