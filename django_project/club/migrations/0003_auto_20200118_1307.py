# Generated by Django 3.0.1 on 2020-01-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20200102_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
