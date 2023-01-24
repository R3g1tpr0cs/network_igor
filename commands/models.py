from django.db import models

class Commands(models.Model):
    input = models.TextField('Ввод команд',)
    output = models.TextField('Вывод команд',)

    def __str__(self):
        return self.input

    class Meta:
        verbose_name = 'Команды'
        verbose_name_plural = 'Команды'