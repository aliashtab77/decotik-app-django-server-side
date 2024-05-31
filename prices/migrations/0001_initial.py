# Generated by Django 5.0.6 on 2024-05-24 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('z1', models.CharField(max_length=255, verbose_name='سازه f47')),
                ('z2', models.CharField(max_length=255, verbose_name='سازه l25')),
                ('z3', models.CharField(max_length=255, verbose_name='اتصال کامل f47')),
                ('z4', models.CharField(max_length=255, verbose_name='اتصال مستقیم ct205')),
                ('z5', models.CharField(max_length=255, verbose_name='بست اتصال طولی f47')),
                ('z6', models.CharField(max_length=255, verbose_name='پروفیل uh36')),
                ('z7', models.CharField(max_length=255, verbose_name='اتصال سقفی ht90')),
                ('z8', models.CharField(max_length=255, verbose_name='نوار ترن فیکس')),
                ('z9', models.CharField(max_length=255, verbose_name='LN11')),
                ('z10', models.CharField(max_length=255, verbose_name='میخ مهاری فولادی سقفی')),
                ('z11', models.CharField(max_length=255, verbose_name='پیچ رولپلاک m6*60mm')),
                ('z12', models.CharField(max_length=255, verbose_name='RG 12.5')),
                ('z13', models.CharField(max_length=255, verbose_name='TN25')),
                ('z14', models.CharField(max_length=255, verbose_name='بتونه درز گیر')),
                ('z15', models.CharField(max_length=255, verbose_name='پودر ماستیک (1)')),
                ('z16', models.CharField(max_length=255, verbose_name='نوار درزگیر')),
            ],
            options={
                'verbose_name_plural': 'لیست قیمت ها',
            },
        ),
    ]