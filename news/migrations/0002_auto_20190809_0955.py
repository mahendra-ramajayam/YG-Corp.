# Generated by Django 2.2.4 on 2019-08-09 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('custom_title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'News Landing Page',
                'verbose_name_plural': 'News Landing Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='newspage',
            options={'verbose_name': 'News Page', 'verbose_name_plural': 'News Page'},
        ),
    ]
