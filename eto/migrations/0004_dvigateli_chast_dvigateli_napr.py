# Generated by Django 5.0.6 on 2024-06-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eto', '0003_alter_dvigateli_tip_1_alter_dvigateli_tip_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvigateli',
            name='chast',
            field=models.IntegerField(default=1, max_length=100, verbose_name='Частота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dvigateli',
            name='napr',
            field=models.IntegerField(default=1, max_length=100, verbose_name='Напряжение'),
            preserve_default=False,
        ),
    ]
