# Generated by Django 4.1.7 on 2023-02-18 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0004_alter_cosecha_areafrascoscosecha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siembra',
            old_name='cosechaFK',
            new_name='cosechaFKSiembra',
        ),
        migrations.AddField(
            model_name='crio',
            name='cosechaFKCrio',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='formularios.cosecha'),
        ),
    ]