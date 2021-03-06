# Generated by Django 3.1.7 on 2021-04-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College', models.TextField()),
                ('CollegeAddress', models.TextField()),
                ('AcademicYear', models.TextField()),
                ('Department', models.TextField()),
                ('Division', models.DecimalField(decimal_places=0, max_digits=10)),
                ('RollNo', models.DecimalField(decimal_places=0, max_digits=10)),
                ('LinkedIn', models.URLField()),
                ('GithubUrl', models.URLField()),
                ('InstagramUrl', models.URLField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
