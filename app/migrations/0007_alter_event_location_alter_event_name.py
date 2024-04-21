# Generated by Django 5.0.4 on 2024-04-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=100, verbose_name="Lieu de l'evenement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=200, verbose_name="Nom de l'evenement"),
        ),
    ]