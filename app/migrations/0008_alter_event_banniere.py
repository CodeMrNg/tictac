# Generated by Django 5.0.4 on 2024-04-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_event_location_alter_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banniere',
            field=models.FileField(upload_to='bannieres/', verbose_name="Affiche de l'evenement"),
        ),
    ]
