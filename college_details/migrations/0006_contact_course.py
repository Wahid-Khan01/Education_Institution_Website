# Generated by Django 5.0.1 on 2024-03-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_details', '0005_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tenure', models.CharField(max_length=50)),
            ],
        ),
    ]
