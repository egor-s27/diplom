from django.db import models

VID_CHOICES = [
        ('Синхронные двигатели', 'Синхронные двигатели'),
        ('Асинхронные двигатели', 'Асинхронные двигатели'),
        ('Вентильные двигатель-генераторы', 'Вентильные двигатель-генераторы'),
    ]

VID_METOD = [
        ('Метод стандартных отклонений', 'Метод стандартных отклонений'),
        ('Метод медианы Кемени', 'Метод медианы Кемени'),
    ]

class Znaniya(models.Model):
    vid_eto = models.CharField('Вид ЭТО', max_length=100, choices=VID_CHOICES)
    vid_metod = models.CharField('Вид метода', max_length=100, choices=VID_METOD)
    otl_koleb = models.FloatField('Отклонение и колебание напряжения')
    nes = models.FloatField('Нессиметрия')
    sin = models.FloatField('Несинусоидальность')
    otl_chast = models.FloatField('Отклонение частоты')
    pomehi = models.FloatField('Электромагнитные помехи')

    def __str__(self):
        return self.vid_eto

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'


