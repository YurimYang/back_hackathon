# Generated by Django 3.1.2 on 2021-07-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Field_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Field_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field3', models.CharField(max_length=100)),
            ],
        ),
    ]