# Generated by Django 2.2.4 on 2019-09-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_auto_20190821_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='address_line_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
