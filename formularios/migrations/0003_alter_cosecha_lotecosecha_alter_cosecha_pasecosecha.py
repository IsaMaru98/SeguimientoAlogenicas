# Generated by Django 4.1.7 on 2023-02-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0002_crio_cosecha_lotecosecha_siembra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosecha',
            name='loteCosecha',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='cosecha',
            name='paseCosecha',
            field=models.TextField(max_length=50),
        ),
    ]
