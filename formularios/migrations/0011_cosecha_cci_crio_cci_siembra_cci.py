# Generated by Django 4.1.7 on 2023-02-21 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0010_alter_crio_cosechafkcrio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosecha',
            name='cci',
            field=models.CharField(default='C0000000', max_length=10),
        ),
        migrations.AddField(
            model_name='crio',
            name='cci',
            field=models.CharField(default='C0000000', max_length=10),
        ),
        migrations.AddField(
            model_name='siembra',
            name='cci',
            field=models.CharField(default='C0000000', max_length=10),
        ),
    ]
