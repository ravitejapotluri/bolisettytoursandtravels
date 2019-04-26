# Generated by Django 2.0.6 on 2018-12-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('customer', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=225)),
                ('email', models.EmailField(default='', max_length=225)),
                ('mobile', models.CharField(default='', max_length=225)),
                ('destination', models.CharField(default='', max_length=225)),
                ('date', models.CharField(default='', max_length=225)),
            ],
        ),
    ]
