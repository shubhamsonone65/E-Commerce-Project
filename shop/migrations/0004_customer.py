# Generated by Django 3.1.7 on 2021-04-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210401_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField(default=None)),
                ('pass1', models.CharField(max_length=300)),
            ],
        ),
    ]
