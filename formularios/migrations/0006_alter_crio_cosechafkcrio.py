# Generated by Django 4.1.7 on 2023-02-18 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0005_rename_cosechafk_siembra_cosechafksiembra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crio',
            name='cosechaFKCrio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.cosecha'),
        ),
    ]
