from django.db import models

VID_CHOICES = [
        ('Синхронный двигатель', 'Синхронный двигатель'),
        ('Асинхронный двигатель', 'Асинхронный двигатель'),
        ('Вентильный двигатель-генератор', 'Вентильный двигатель-генератор'),
    ]

class Dvigateli(models.Model):
    model = models.CharField('Название модели', max_length=100, default='') #поле до 255 символов
    vid_eto = models.CharField('Вид ЭТО', max_length=100, choices=VID_CHOICES)
    tip_1 = models.BooleanField('Основные', default=False)
    tip_2 = models.BooleanField('Дополнительные', default=False)
    tip_3 = models.BooleanField('Вспомогательные', default=False)
    napr = models.IntegerField('Напряжение',max_length=100)
    chast = models.IntegerField('Частота',max_length=100)

    # Указываем в виде какой информации будет отображаться объект таблицы,
    # в нашем случае в виде названия модели оборудования
    def __str__(self):
        return self.model

    #Адрес по которому переходит программа после изменения записи ЭТО
    def get_absolute_url(self):
        return f'/eto/{self.id}'

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'
# Create your models here.
#models.TextField - большое поле 30 тыс символов
#models.DateField - дата
#models.DateTimeField - дата и время

