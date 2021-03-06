# Generated by Django 3.0.6 on 2020-06-04 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_content', models.CharField(max_length=240)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
    ]
