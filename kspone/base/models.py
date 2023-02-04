from django.db import models

# Create your models here.
class Ksp(models.Model):
    person_name=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    district_Name=models.CharField(max_length=200)
    PS_Name=models.CharField(max_length=200)
    fir_no=models.CharField(max_length=200)
    fir_date=models.DateField()
    person_No=models.CharField(max_length=200)
    arrest_Date=models.DateField()
    father_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    ageWhileOpening=models.DateField()
    age=models.DateField()
    pres_address1=models.TextField(max_length=200)
    perm_address1=models.TextField(max_length=200)
    person_status=models.CharField(max_length=200)
    major_head=models.CharField(max_length=200)
    minor_head=models.CharField(max_length=200)
    crime_no=models.IntegerField()
    arr_id=models.IntegerField()
    unit_id=models.IntegerField()
    fir_id=models.DateField()
    dedt=models.DateTimeField()



