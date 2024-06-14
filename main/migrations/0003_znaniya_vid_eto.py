# Generated by Django 5.0.6 on 2024-06-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_znaniya_options_alter_znaniya_nes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='znaniya',
            name='vid_eto',
            field=models.CharField(choices=[('Синхронный двигатель', 'Синхронный двигатель'), ('Асинхронный двигатель', 'Асинхронный двигатель'), ('Вентильный двигатель-генератор', 'Вентильный двигатель-генератор')], default=1, max_length=100, verbose_name='Вид ЭТО'),
            preserve_default=False,
        ),
    ]
