# Generated by Django 3.0.6 on 2020-06-05 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profilestatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilestatus',
            options={'verbose_name_plural': 'statuses'},
        ),
    ]
