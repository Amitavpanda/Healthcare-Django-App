# Generated by Django 3.2.7 on 2021-10-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thehealth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Event Name '),
        ),
    ]
