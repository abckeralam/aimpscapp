# Generated by Django 4.1.3 on 2022-11-07 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aimapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]