from django.db import models
from account.models import Startup,Mentor,Account
# Create your models here.
class Meeting(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    link = models.TextField(null=True, blank=True)
    about = models.TextField()
    goals = models.TextField()
    expectations = models.TextField()
    querries = models.TextField()
    date=models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    # objects= MyAccountManager()
    def __str__(self):
        return self.date

class TempMeeting(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    about = models.TextField()
    goals = models.TextField()
    expectations = models.TextField()
    querries = models.TextField()
    time=models.TimeField()
    date=models.DateField()
    is_completed = models.BooleanField(default=False)

    # objects= MyAccountManager()
    def __str__(self):
        return self.startup.startup_name