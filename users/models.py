from django.db import models

class User(models.Model):
    surname = models.CharField('Фамилия', max_length=100) #поле до 255 символов
    name = models.CharField('Имя', max_length=100)  # поле до 255 символов
    mid_name = models.CharField('Отчество', max_length=100)  # поле до 255 символов
    dostup = models.BooleanField('Администратор', default=False)
    phone = models.CharField('Телефон', max_length=12) #поле до 255 символов
    login = models.CharField('Логин', max_length=100) #поле до 255 символов
    pas = models.CharField('Пароль', max_length=100) #поле до 255 символов

    # Указываем в виде какой информации будет отображаться объект таблицы,
    # в нашем случае в виде названия модели оборудования
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'

# Create your models here.
