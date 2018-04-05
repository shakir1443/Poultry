from django.db import models
import datetime
# Create your models here.
class data(models.Model):
    Day = models.IntegerField(max_length=11)
    Temperature = models.FloatField(max_length=50)
    Humidity = models.FloatField(max_length=50)
    Carbon_dy_oxide = models.FloatField(max_length=50)
    Amonia = models.FloatField(max_length=50)
    ADC=models.CharField(max_length=100)
    Light_status= models.CharField(max_length=100)
    Fan_status = models.CharField(max_length=100)
    Start_date = models.DateField()
    Cur_Date = models.DateField()
    Cur_time = models.TimeField(null=True, blank=True)
    Restart_no = models.IntegerField(max_length=11)
   # Restart_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = "data"
