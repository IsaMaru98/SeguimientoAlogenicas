# Generated by Django 4.1.7 on 2023-02-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0019_cosecha_confluenciacosecha_cosecha_tiempocultivodias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siembra',
            name='id',
        ),
        migrations.AddField(
            model_name='siembra',
            name='siembraId',
            field=models.CharField(default='01-01-2000-25-1-001', max_length=50, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
