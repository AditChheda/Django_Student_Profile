# Generated by Django 3.1.7 on 2021-04-13 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userinformation_profilepicture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='ProfilePicture',
        ),
    ]