# Generated by Django 2.1.7 on 2019-08-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20190819_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traininglead',
            name='followup',
            field=models.DateField(null=True),
        ),
    ]
