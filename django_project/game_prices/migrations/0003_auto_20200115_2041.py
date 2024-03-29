# Generated by Django 3.0.1 on 2020-01-15 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game_prices', '0002_auto_20200102_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameprice',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='gameprice',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='gameprice',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
