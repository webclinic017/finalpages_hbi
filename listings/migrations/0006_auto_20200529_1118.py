# Generated by Django 2.2 on 2020-05-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20200527_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='preview_1',
            field=models.ImageField(blank=True, upload_to='documents/previews/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='preview_2',
            field=models.ImageField(blank=True, upload_to='documents/previews/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='preview_3',
            field=models.ImageField(blank=True, upload_to='documents/previews/%Y/%m/%d/'),
        ),
    ]