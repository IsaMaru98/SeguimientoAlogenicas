# Generated by Django 4.1.5 on 2023-03-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0027_crio_cosecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='dato',
            name='cci',
            field=models.CharField(default='', max_length=10),
        ),
    ]
