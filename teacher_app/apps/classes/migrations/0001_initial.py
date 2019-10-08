# Generated by Django 2.2.6 on 2019-10-08 11:27

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
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50, verbose_name="Students's first name")),
                ('lastName', models.CharField(max_length=50, verbose_name="Students's last name")),
                ('age', models.IntegerField()),
                ('regNumber', models.CharField(max_length=50, unique=True, verbose_name='Students registration number')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubjectMath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('assign', models.BooleanField(default=False)),
                ('student_reg_num', models.CharField(max_length=254, unique=True)),
                ('className', models.CharField(max_length=254)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubjectEng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('assign', models.BooleanField(default=False)),
                ('student_reg_num', models.CharField(max_length=254, unique=True)),
                ('className', models.CharField(max_length=254)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=254, unique=True, verbose_name='Name of the class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='className',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.StudentClass'),
        ),
    ]
