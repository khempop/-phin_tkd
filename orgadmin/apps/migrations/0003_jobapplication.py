# Generated by Django 3.2 on 2023-01-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20230104_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/job/application')),
                ('company_name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('apply_date', models.DateField()),
                ('contact', models.CharField(max_length=13)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('New', 'New'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], max_length=15)),
                ('type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15)),
            ],
        ),
    ]
