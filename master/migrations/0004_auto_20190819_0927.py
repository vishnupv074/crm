# Generated by Django 2.1.7 on 2019-08-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_traininglead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traininglead',
            name='followup',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='traininglead',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]