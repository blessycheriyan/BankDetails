from django.db import models

class Bankdetails(models.Model):
    bank_id=models.CharField(max_length=10)
    ifsc_code=models.CharField(max_length=8)
    branch_name=models.CharField(max_length=25)
    address=models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    district=models.CharField(max_length=35)
    state = models.CharField(max_length=36)
    bank_name=models.CharField(max_length=35)
