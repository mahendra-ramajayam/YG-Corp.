# Generated by Django 2.2.5 on 2019-09-30 14:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0015_menusnippet_global_navigation_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusnippet',
            name='menu_links',
            field=wagtail.core.fields.StreamField([('social_channel_links', wagtail.core.blocks.StructBlock([('menu_navigation_level_1', wagtail.core.blocks.StreamBlock([('menu_external_url', wagtail.core.blocks.StructBlock([('displayed_name', wagtail.core.blocks.CharBlock(max_length=32, required=True)), ('url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], help_text='choose url', required=True)), ('menu_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True))], help_text='choose page', required=True)), ('navigation_html_id', wagtail.core.blocks.CharBlock(max_length=16, required=True)), ('link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Link or file title', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.core.blocks.StreamBlock([('menu_external_url', wagtail.core.blocks.StructBlock([('displayed_name', wagtail.core.blocks.CharBlock(max_length=32, required=True)), ('url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], help_text='choose url', required=True)), ('menu_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose doc file', required=True))], required=False)), ('if_document_pdf', wagtail.core.blocks.ChoiceBlock(choices=[('Download', 'Download'), ('Open', 'Open')], help_text='choose either download or open pdf file', required=False))])), ('menu_navigation_level_2', wagtail.core.blocks.StreamBlock([('menu_external_url', wagtail.core.blocks.StructBlock([('displayed_name', wagtail.core.blocks.CharBlock(max_length=32, required=True)), ('url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], help_text='choose url', required=True)), ('menu_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True))], help_text='add nested pages', required=False))]))], blank=True, null=True),
        ),
    ]