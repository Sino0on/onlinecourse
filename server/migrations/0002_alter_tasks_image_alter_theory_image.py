# Generated by Django 4.0.3 on 2022-03-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='image',
            field=models.ImageField(blank=True, upload_to='tasks/'),
        ),
        migrations.AlterField(
            model_name='theory',
            name='image',
            field=models.ImageField(blank=True, upload_to='theory'),
        ),
    ]
