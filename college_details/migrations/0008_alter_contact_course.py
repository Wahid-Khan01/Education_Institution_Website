# Generated by Django 5.0.1 on 2024-04-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_details', '0007_alter_contact_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.CharField(max_length=100),
        ),
    ]
