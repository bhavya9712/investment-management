# Generated by Django 3.1.2 on 2022-04-16 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investment', '0001_initial'),
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminders',
            name='Reminder_Investment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.investment'),
        ),
        migrations.AlterField(
            model_name='reminders',
            name='Reminder_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]