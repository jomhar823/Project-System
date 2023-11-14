# Generated by Django 4.2.6 on 2023-11-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapp', '0007_alter_report_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('origin', models.CharField(max_length=50)),
            ],
        ),
    ]
