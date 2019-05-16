# Generated by Django 2.2.1 on 2019-05-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=512, null=True)),
                ('contactType', models.CharField(max_length=52, null=True)),
                ('contact', models.CharField(max_length=512, null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(editable=False)),
                ('lastModifiedDate', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('joinId', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=512, null=True)),
                ('contactType', models.CharField(choices=[('whatsapp', 'Whatsapp'), ('line', 'Line'), ('email', 'Email')], max_length=52)),
                ('contact', models.CharField(max_length=512, null=True)),
                ('pickupPoint', models.CharField(max_length=2056, null=True)),
                ('dropoffPoint', models.CharField(max_length=2056, null=True)),
                ('pickupDate', models.DateField(null=True)),
                ('pickupTime', models.TimeField(null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(editable=False)),
                ('lastModifiedDate', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'join',
            },
        ),
        migrations.CreateModel(
            name='Later',
            fields=[
                ('laterId', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=512, null=True)),
                ('contactType', models.CharField(choices=[('whatsapp', 'Whatsapp'), ('line', 'Line'), ('email', 'Email')], max_length=52)),
                ('contact', models.CharField(max_length=512, null=True)),
                ('activityArea', models.CharField(max_length=1024, null=True)),
                ('whyNotNow', models.TextField(null=True)),
                ('suggestion', models.TextField(null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(editable=False)),
                ('lastModifiedDate', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'later',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionId', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=512, null=True)),
                ('contactType', models.CharField(choices=[('whatsapp', 'Whatsapp'), ('line', 'Line'), ('email', 'Email')], max_length=52)),
                ('contact', models.CharField(max_length=512, null=True)),
                ('question', models.TextField(null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(editable=False)),
                ('lastModifiedDate', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
