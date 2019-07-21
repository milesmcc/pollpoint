from django.contrib import admin

from .models import Poll, PollChoice, PollOption, SessionUser

# Register your models here.
admin.site.register(Poll)
admin.site.register(PollChoice)
admin.site.register(PollOption)
admin.site.register(SessionUser)