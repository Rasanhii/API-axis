# Generated by Django 5.0.2 on 2024-04-19 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtos',
            old_name='nome',
            new_name='produto',
        ),
    ]
