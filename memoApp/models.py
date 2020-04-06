from django.db import models
import datetime
# Create your models here.

class Habbit(models.Model):
    habbitName=models.CharField(max_length=13)
    start_datetime=datetime.datetime.now()
    startDate=models.CharField(max_length=30)
    progress=models.CharField(max_length=66)
    finishDate=models.CharField(max_length=30)
    daysCount=models.SmallIntegerField()
    daysFail=models.SmallIntegerField()
    daysSucceed = models.SmallIntegerField()
    give_up=models.BooleanField(default=False)
    givenup_date=models.CharField(max_length=30)


class Memo(models.Model):
    today=datetime.datetime.now()
    date_time=today.strftime('%Y/%m/%d')
    contents=models.TextField()
    habbit=models.ForeignKey(Habbit, on_delete=models.PROTECT)
