# Generated by Django 4.1.4 on 2023-01-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switches',
            name='ip',
            field=models.IntegerField(verbose_name='IP-адрес'),
        ),
        migrations.AlterField(
            model_name='switches',
            name='soft_version',
            field=models.IntegerField(verbose_name='Версия прошивки'),
        ),
    ]
