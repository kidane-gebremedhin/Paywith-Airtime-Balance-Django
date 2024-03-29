# Generated by Django 3.0.1 on 2020-01-02 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home_or_away_status', '0002_auto_20200102_2045'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketCode', models.CharField(max_length=255)),
                ('fullName', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=13, null=True)),
                ('paidAmount', models.FloatField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('homeOrAwayStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_or_away_status.HomeOrAwayStatus')),
            ],
        ),
    ]
