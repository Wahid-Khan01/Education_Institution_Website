# Generated by Django 5.0.1 on 2024-03-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_details', '0003_userprofile2'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndiaCities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
