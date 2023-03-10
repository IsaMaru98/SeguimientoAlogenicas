# Generated by Django 4.1.7 on 2023-02-22 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0020_remove_siembra_id_siembra_siembraid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cosecha',
            name='idCosecha',
        ),
        migrations.RemoveField(
            model_name='crio',
            name='cosechaFKCrio',
        ),
        migrations.RemoveField(
            model_name='siembra',
            name='cosechaFKSiembra',
        ),
        migrations.AddField(
            model_name='cosecha',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cosecha',
            name='siembra',
            field=models.ForeignKey(default='c0222001-2000-01-01-25-1-001', on_delete=django.db.models.deletion.CASCADE, to='formularios.siembra'),
            preserve_default=False,
        ),
    ]
