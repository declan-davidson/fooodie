# Generated by Django 2.2.3 on 2020-03-03 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('picture', models.ImageField(blank=True, upload_to='profilepics')),
                ('totalVotes', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('votes', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='photos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooodie.UserProfile')),
            ],
        ),
    ]
