# Generated by Django 3.1.4 on 2021-02-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Sr_No', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True, max_length=100)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('Sr_No', models.AutoField(primary_key=True, serialize=False)),
                ('DESTINATION', models.CharField(blank=True, choices=[('Delhi', 'Delhi'), ('Mumbai', 'Mumbai'), ('Bangalore', 'Bangalore'), ('Bhopal', 'Bhopal'), ('Pune', 'Pune')], max_length=50, null=True)),
                ('ARRIVAL', models.CharField(blank=True, choices=[('Delhi', 'Delhi'), ('Mumbai', 'Mumbai'), ('Bangalore', 'Bangalore'), ('Bhopal', 'Bhopal'), ('Pune', 'Pune')], max_length=50, null=True)),
                ('PASSENGERS', models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('>5', '>5')], null=True)),
                ('Airlines', models.CharField(blank=True, max_length=500, null=True)),
                ('Depart_time', models.CharField(blank=True, max_length=500, null=True)),
                ('Arrival_time', models.CharField(blank=True, max_length=500, null=True)),
                ('Fare', models.IntegerField(blank=True, default=0, null=True)),
                ('Date', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
