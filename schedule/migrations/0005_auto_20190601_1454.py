# Generated by Django 2.2.1 on 2019-06-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_remove_userprofile_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
