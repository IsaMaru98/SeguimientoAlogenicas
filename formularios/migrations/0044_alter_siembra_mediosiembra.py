# Generated by Django 4.2.3 on 2023-08-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0043_alter_dato_mediosiembra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siembra',
            name='medioSiembra',
            field=models.CharField(default='NR', max_length=50),
        ),
    ]
