from django.db import models

class Switches(models.Model):
    name = models.CharField('Название', max_length=30)
    vendor = models.CharField('Производитель оборудования', max_length=15)
    model = models.CharField('Модель оборудования', max_length=20)
    soft_version = models.CharField('Версия прошивки', max_length=20)
    serial_number = models.CharField('Серийный номер', max_length=20)
    ip = models.CharField('IP-адрес', max_length=20)
    location = models.CharField('Местонахождения', max_length=30)
    buiding = models.CharField('Здание', max_length=10)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/switches/{self.id}'
    
    
    class Meta:
        verbose_name = 'Коммутаторы'
        verbose_name_plural = 'Коммутаторы'
