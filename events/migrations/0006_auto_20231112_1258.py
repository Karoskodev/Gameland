# Generated by Django 3.2.23 on 2023-11-12 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_event_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='likes',
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
    ]