# Generated by Django 4.1.7 on 2023-02-14 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bet',
            new_name='Game',
        ),
    ]
