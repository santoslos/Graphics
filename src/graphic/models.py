from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Graphic(models.Model):
    function = models.CharField(max_length=255, verbose_name="Функция")
    step = models.SmallIntegerField(verbose_name="Шаг")
    bot_interval = models.FloatField(verbose_name="Нижний интервал")
    top_interval = models.FloatField(verbose_name="Верхний интервал")
    data = models.DateField(auto_now=True, verbose_name='дата сохранения')
    figure = models.ImageField(upload_to='figures/', blank=True, null=True)

    def __str__(self):
        return f' Функция равна = {self.function}'

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = "Графики"
        ordering = ['data']
