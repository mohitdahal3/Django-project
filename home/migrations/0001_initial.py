# Generated by Django 3.2.2 on 2021-06-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=80)),
                ('phone', models.CharField(default='', max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
