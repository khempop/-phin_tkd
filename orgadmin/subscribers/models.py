from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Subscribers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_customer_id = models.CharField(max_length=100,null=True)
    subscription_id = models.CharField(max_length=100,null=True)
    subscription_status = models.BooleanField(default=False, verbose_name="subscription_status",null=True)
    subscription_exp_date = models.DateField(null=True)