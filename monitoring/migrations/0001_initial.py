# Generated by Django 5.0.1 on 2024-02-26 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=6)),
                ('adress', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('topic', models.CharField(max_length=20)),
                ('info', models.TextField()),
                ('file', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='PrinterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOrganization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('contact', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.TextField()),
                ('id_chat', models.BigIntegerField()),
                ('branchs', models.TextField()),
                ('name', models.CharField(max_length=30)),
                ('col_sq', models.IntegerField()),
                ('monitoring', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('ip', models.CharField(max_length=15)),
                ('status', models.BooleanField()),
                ('monitoring', models.BooleanField()),
                ('time_off', models.DateTimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.branch')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.equipment_type')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('ip', models.TextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.branch')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.printermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.TextField()),
                ('type', models.IntegerField()),
                ('status', models.BooleanField()),
                ('comment', models.TextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.branch')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.serviceorganization')),
            ],
        ),
    ]
