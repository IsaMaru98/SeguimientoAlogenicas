# Generated by Django 4.1.7 on 2023-02-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0012_alter_cosecha_cci_alter_crio_cci_alter_siembra_cci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosecha',
            name='fechaCosecha',
            field=models.DateField(choices=[('P0', 'P0'), ('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7')]),
        ),
    ]
