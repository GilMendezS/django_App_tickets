# Generated by Django 2.1.5 on 2019-01-25 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='status_id',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='user_id',
            new_name='user',
        ),
    ]
