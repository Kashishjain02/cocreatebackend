from django.db import models
from account.models import Account
# Create your models here.

class Transaction(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True, )
    amount = models.IntegerField(null=False, blank=False)
    txn_id = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    # objects= MyAccountManager()
    def __str__(self):
        return self.txn_id