# Generated by Django 4.1.5 on 2023-03-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0028_dato_cci'),
    ]

    operations = [
        migrations.AddField(
            model_name='dato',
            name='loteDatos',
            field=models.FloatField(default=0),
        ),
    ]
