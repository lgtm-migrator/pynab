# Generated by Django 2.1.3 on 2018-11-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surprise_frequency', models.IntegerField(default=30)),
                ('next_surprise', models.DateTimeField(null=True)),
            ],
        ),
    ]
