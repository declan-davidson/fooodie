# Generated by Django 2.2.3 on 2020-03-31 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooodie', '0004_auto_20200329_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
