# Generated by Django 4.0.1 on 2022-04-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profilephoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
