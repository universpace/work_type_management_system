# Generated by Django 4.1.2 on 2022-11-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_team_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='anonymouse_name',
            field=models.CharField(default='', max_length=30, verbose_name='익명이름'),
            preserve_default=False,
        ),
    ]