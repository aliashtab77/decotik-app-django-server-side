from django.shortcuts import render
from prices.models import Prices
from django.http import JsonResponse
# Create your views here.


def get_prices(request):
    prices = Prices.objects.all()[0]
    data = {
        'سازه F47':int(prices.z1),
        'سازه L25':int(prices.z2),
        'اتصال کامل F47':int(prices.z3),
        'اتصال مستقیم CT205':int(prices.z4),
        'بست اتصال طولی F47':int(prices.z5),
        'پروفیل UH36':int(prices.z6),
        'اتصال سقفی HT90':int(prices.z7),
        'نوار ترن فیکس':int(prices.z8),
        'LN11':int(prices.z9),
        'میخ مهاری فولادی سقفی m6*40mm':int(prices.z10),
        'پیچ رولپلاگ m6*60mm':int(prices.z11),
        'RG 12.5':int(prices.z12),
        'TN25':int(prices.z13),
        'بتونه درزگیر':int(prices.z14),
        'پودر ماستیک(1)':int(prices.z15),
        'نوار درزگیر':int(prices.z16),

    }

    return JsonResponse(data)