# Generated by Django 4.0.1 on 2022-04-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_customuser_profilephoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profilephoto',
            field=models.ImageField(blank=True, default='OIP.jpeg', null=True, upload_to='media/'),
        ),
    ]
