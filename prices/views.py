from django.shortcuts import render
from prices.models import Prices, Prices042, Prices046, Prices048, Prices055, Prices058
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
        'سازه CD60':int(prices.z17),
        'سازه تراز UD28':int(prices.z18),
        'اتصال کامل CD60':int(prices.z19),
        'بست اتصال طولی CD60':int(prices.z20),
        'آویز نانیوس *':int(prices.z21),
        'سازه رانر U50':int(prices.z22),
        'پنل آکوستیک پانچ دایره ای نامنظم 12/20/35':int(prices.z23),
        'TN25/ SN30':int(prices.z24),
        'بتونه TRIAS':int(prices.z25),
        'سازه استاد C50':int(prices.z26),
        'نوار عایق پشت چسبدار 4*15':int(prices.z27),
        'سازه استاد CW50':int(prices.z28),
        'سازه رانر UW50':int(prices.z29),
        'سازه استاد C70':int(prices.z30),
        'سازه رانر U70':int(prices.z31),
        'سازه استاد CW75':int(prices.z32),
        'سازه رانر UW75':int(prices.z33),
        'سازه استاد C100':int(prices.z34),
        'سازه رانر U100':int(prices.z35),
        'سازه استاد CW100':int(prices.z36),
        'سازه رانر UW100':int(prices.z37),
        'TN35':int(prices.z38),

    }

    return JsonResponse(data)




def get_prices042(request):
    prices = Prices042.objects.all()[0]
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
        'سازه CD60':int(prices.z17),
        'سازه تراز UD28':int(prices.z18),
        'اتصال کامل CD60':int(prices.z19),
        'بست اتصال طولی CD60':int(prices.z20),
        'آویز نانیوس *':int(prices.z21),
        'سازه رانر U50':int(prices.z22),
        'پنل آکوستیک پانچ دایره ای نامنظم 12/20/35':int(prices.z23),
        'TN25/ SN30':int(prices.z24),
        'بتونه TRIAS':int(prices.z25),
        'سازه استاد C50':int(prices.z26),
        'نوار عایق پشت چسبدار 4*15':int(prices.z27),
        'سازه استاد CW50':int(prices.z28),
        'سازه رانر UW50':int(prices.z29),
        'سازه استاد C70':int(prices.z30),
        'سازه رانر U70':int(prices.z31),
        'سازه استاد CW75':int(prices.z32),
        'سازه رانر UW75':int(prices.z33),
        'سازه استاد C100':int(prices.z34),
        'سازه رانر U100':int(prices.z35),
        'سازه استاد CW100':int(prices.z36),
        'سازه رانر UW100':int(prices.z37),
        'TN35':int(prices.z38),

    }

    return JsonResponse(data)




def get_prices046(request):
    prices = Prices046.objects.all()[0]
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
        'سازه CD60':int(prices.z17),
        'سازه تراز UD28':int(prices.z18),
        'اتصال کامل CD60':int(prices.z19),
        'بست اتصال طولی CD60':int(prices.z20),
        'آویز نانیوس *':int(prices.z21),
        'سازه رانر U50':int(prices.z22),
        'پنل آکوستیک پانچ دایره ای نامنظم 12/20/35':int(prices.z23),
        'TN25/ SN30':int(prices.z24),
        'بتونه TRIAS':int(prices.z25),
        'سازه استاد C50':int(prices.z26),
        'نوار عایق پشت چسبدار 4*15':int(prices.z27),
        'سازه استاد CW50':int(prices.z28),
        'سازه رانر UW50':int(prices.z29),
        'سازه استاد C70':int(prices.z30),
        'سازه رانر U70':int(prices.z31),
        'سازه استاد CW75':int(prices.z32),
        'سازه رانر UW75':int(prices.z33),
        'سازه استاد C100':int(prices.z34),
        'سازه رانر U100':int(prices.z35),
        'سازه استاد CW100':int(prices.z36),
        'سازه رانر UW100':int(prices.z37),
        'TN35':int(prices.z38),

    }

    return JsonResponse(data)





def get_prices048(request):
    prices = Prices048.objects.all()[0]
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
        'سازه CD60':int(prices.z17),
        'سازه تراز UD28':int(prices.z18),
        'اتصال کامل CD60':int(prices.z19),
        'بست اتصال طولی CD60':int(prices.z20),
        'آویز نانیوس *':int(prices.z21),
        'سازه رانر U50':int(prices.z22),
        'پنل آکوستیک پانچ دایره ای نامنظم 12/20/35':int(prices.z23),
        'TN25/ SN30':int(prices.z24),
        'بتونه TRIAS':int(prices.z25),
        'سازه استاد C50':int(prices.z26),
        'نوار عایق پشت چسبدار 4*15':int(prices.z27),
        'سازه استاد CW50':int(prices.z28),
        'سازه رانر UW50':int(prices.z29),
        'سازه استاد C70':int(prices.z30),
        'سازه رانر U70':int(prices.z31),
        'سازه استاد CW75':int(prices.z32),
        'سازه رانر UW75':int(prices.z33),
        'سازه استاد C100':int(prices.z34),
        'سازه رانر U100':int(prices.z35),
        'سازه استاد CW100':int(prices.z36),
        'سازه رانر UW100':int(prices.z37),
        'TN35':int(prices.z38),

    }

    return JsonResponse(data)




def get_prices055(request):
    prices = Prices055.objects.all()[0]
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
        'سازه CD60':int(prices.z17),
        'سازه تراز UD28':int(prices.z18),
        'اتصال کامل CD60':int(prices.z19),
        'بست اتصال طولی CD60':int(prices.z20),
        'آویز نانیوس *':int(prices.z21),
        'سازه رانر U50':int(prices.z22),
        'پنل آکوستیک پانچ دایره ای نامنظم 12/20/35':int(prices.z23),
        'TN25/ SN30':int(prices.z24),
        'بتونه TRIAS':int(prices.z25),
        'سازه استاد C50':int(prices.z26),
        'نوار عایق پشت چسبدار 4*15':int(prices.z27),
        'سازه استاد CW50':int(prices.z28),
        'سازه رانر UW50':int(prices.z29),
        'سازه استاد C70':int(prices.z30),
        'سازه رانر U70':int(prices.z31),
        'سازه استاد CW75':int(prices.z32),
        'سازه رانر UW75':int(prices.z33),
        'سازه استاد C100':int(prices.z34),
        'سازه رانر U100':int(prices.z35),
        'سازه استاد CW100':int(prices.z36),
        'سازه رانر UW100':int(prices.z37),
        'TN35':int(prices.z38),

    }

    return JsonResponse(data)




def get_prices058(request):
    prices = Prices058.objects.all()[0]
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
        'سازه CD60':int(prices.z17),
        'سازه تراز UD28':int(prices.z18),
        'اتصال کامل CD60':int(prices.z19),
        'بست اتصال طولی CD60':int(prices.z20),
        'آویز نانیوس *':int(prices.z21),
        'سازه رانر U50':int(prices.z22),
        'پنل آکوستیک پانچ دایره ای نامنظم 12/20/35':int(prices.z23),
        'TN25/ SN30':int(prices.z24),
        'بتونه TRIAS':int(prices.z25),
        'سازه استاد C50':int(prices.z26),
        'نوار عایق پشت چسبدار 4*15':int(prices.z27),
        'سازه استاد CW50':int(prices.z28),
        'سازه رانر UW50':int(prices.z29),
        'سازه استاد C70':int(prices.z30),
        'سازه رانر U70':int(prices.z31),
        'سازه استاد CW75':int(prices.z32),
        'سازه رانر UW75':int(prices.z33),
        'سازه استاد C100':int(prices.z34),
        'سازه رانر U100':int(prices.z35),
        'سازه استاد CW100':int(prices.z36),
        'سازه رانر UW100':int(prices.z37),
        'TN35':int(prices.z38),

    }

    return JsonResponse(data)

