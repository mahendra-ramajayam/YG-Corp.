# Generated by Django 2.2.4 on 2019-08-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190809_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='link_tab_chooser',
            field=models.CharField(choices=[('_blank', 'Current tab'), ('_self', 'New tab')], default='_blank', max_length=6),
        ),
    ]