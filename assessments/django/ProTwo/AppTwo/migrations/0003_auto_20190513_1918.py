# Generated by Django 2.2 on 2019-05-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0002_auto_20190513_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=264),
        ),
    ]
