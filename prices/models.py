from django.db import models

# Create your models here.



class Prices(models.Model):

    z1 = models.CharField(max_length=255, verbose_name="سازه f47")
    z2 = models.CharField(max_length=255, verbose_name="سازه l25")
    z3 = models.CharField(max_length=255, verbose_name="اتصال کامل f47")
    z4 = models.CharField(max_length=255, verbose_name="اتصال مستقیم ct205")
    z5 = models.CharField(max_length=255, verbose_name='بست اتصال طولی f47')
    z6 = models.CharField(max_length=255, verbose_name='پروفیل uh36')
    z7 = models.CharField(max_length=255, verbose_name='اتصال سقفی ht90')
    z8 = models.CharField(max_length=255, verbose_name='نوار ترن فیکس')
    z9 = models.CharField(max_length=255, verbose_name='LN11')
    z10 = models.CharField(max_length=255, verbose_name='میخ مهاری فولادی سقفی')
    z11 = models.CharField(max_length=255, verbose_name='پیچ رولپلاک m6*60mm')
    z12 = models.CharField(max_length=255, verbose_name='RG 12.5')
    z13 = models.CharField(max_length=255, verbose_name='TN25')
    z14 = models.CharField(max_length=255, verbose_name='بتونه درز گیر')
    z15 = models.CharField(max_length=255, verbose_name='پودر ماستیک (1)')
    z16 = models.CharField(max_length=255, verbose_name='نوار درزگیر')
    z17 = models.CharField(max_length=255, verbose_name='سازه CD60')
    z18 = models.CharField(max_length=255, verbose_name='سازه تراز UD28')
    z19 = models.CharField(max_length=255, verbose_name='اتصال کامل CD60')
    z20 = models.CharField(max_length=255, verbose_name='بست اتصال طولی CD60')
    z21 = models.CharField(max_length=255, verbose_name='آویز نانیوس *')
    z22 = models.CharField(max_length=255, verbose_name='سازه رانر U50')
    z23 = models.CharField(max_length=255, verbose_name='پنل آکوستیک پانچ دایره ای نامنظم 12/20/35')
    z24 = models.CharField(max_length=255, verbose_name='TN25/ SN30')
    z25 = models.CharField(max_length=255, verbose_name='بتونه TRIAS')



    class Meta:
        verbose_name_plural = "لیست قیمت های kplus"

