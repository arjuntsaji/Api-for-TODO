# Generated by Django 3.1.7 on 2021-06-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
