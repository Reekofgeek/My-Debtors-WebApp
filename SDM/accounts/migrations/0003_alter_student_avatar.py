# Generated by Django 4.0.6 on 2022-08-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_guardianchild_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.FileField(default='static/images/avatar/blank-profile-picture.png', max_length=255, upload_to='static/images/avatar/profile_img'),
        ),
    ]