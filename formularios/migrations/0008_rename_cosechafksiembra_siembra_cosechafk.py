# Generated by Django 4.1.7 on 2023-02-18 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0007_remove_crio_cosechafkcrio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siembra',
            old_name='cosechaFKSiembra',
            new_name='cosechaFK',
        ),
    ]
