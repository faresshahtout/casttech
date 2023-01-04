from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
class casts_scan(models.Model):
    Doctor=models.ForeignKey(User,on_delete=models.CASCADE,unique=False)
    patientname=models.TextField(default="john doe")
    file=models.FileField()
class casts(models.Model):
    Doctor=models.ForeignKey(User,on_delete=models.CASCADE,unique=False)
    patientname=models.TextField(default="john doe")
    wristwidth=models.DecimalField(decimal_places=2,max_digits=90000)
    wristhight=models.DecimalField(decimal_places=2,max_digits=90000)
    clearence=models.DecimalField(decimal_places=2,max_digits=90000)
    ABsection=models.DecimalField(decimal_places=2,max_digits=90000)
    Bwidth=models.DecimalField(decimal_places=2,max_digits=90000)
    Bhight=models.DecimalField(decimal_places=2,max_digits=90000)
    castthinkniss=models.DecimalField(decimal_places=2,max_digits=90000)
    BCsection=models.DecimalField(decimal_places=2,max_digits=90000)
    Cheight=models.DecimalField(decimal_places=2,max_digits=90000)
    Cwidth=models.DecimalField(decimal_places=2,max_digits=90000)
    circulediameter=models.DecimalField(decimal_places=2,max_digits=90000)
    leftpump=models.DecimalField(decimal_places=2,max_digits=90000)
    handtip=models.DecimalField(decimal_places=2,max_digits=90000)
    rightpump=models.DecimalField(decimal_places=2,max_digits=90000)
    midhandthikness=models.DecimalField(decimal_places=2,max_digits=90000)
    palmlength=models.DecimalField(decimal_places=2,max_digits=90000)
    palmwidth=models.DecimalField(decimal_places=2,max_digits=90000)
    thumbmusile=models.DecimalField(decimal_places=2,max_digits=90000)
    pattrebdensity=models.DecimalField(decimal_places=2,max_digits=90000,default=5)
    patternlength=models.DecimalField(decimal_places=2,max_digits=90000,default=5)

# 0770254420 lauras number call on sunday
