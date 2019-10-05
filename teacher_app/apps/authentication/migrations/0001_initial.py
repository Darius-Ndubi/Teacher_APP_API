# Generated by Django 2.2.6 on 2019-10-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstName', models.CharField(max_length=50, verbose_name="User's first name")),
                ('lastName', models.CharField(max_length=50, verbose_name="User's last name")),
                ('username', models.CharField(max_length=50, unique=True, verbose_name="User's username")),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name="User's email")),
                ('is_teacher', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]