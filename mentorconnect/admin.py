from django.contrib import admin
from mentorconnect.models import Meeting,TempMeeting,Applications

# Register your models here.

admin.site.register(Meeting)
admin.site.register(TempMeeting)
admin.site.register(Applications)
