# Generated by Django 3.2.3 on 2021-05-17 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='browserpolicy',
            old_name='policy_id',
            new_name='policy',
        ),
        migrations.RenameField(
            model_name='browserpolicy',
            old_name='site_id',
            new_name='site',
        ),
        migrations.RenameField(
            model_name='clientpolicy',
            old_name='client_id',
            new_name='client',
        ),
    ]
