# Generated by Django 5.0 on 2023-12-17 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmoperson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]