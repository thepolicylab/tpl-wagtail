# Generated by Django 2.0 on 2020-03-08 04:55

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyWritingSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(help_text='Hero Header', max_length=255)),
                ('hero_lead', wagtail.core.fields.RichTextField(help_text='Hero Lead Text', max_length=255)),
                ('hero_cta_text', models.CharField(help_text='Hero CTA Text', max_length=255)),
                ('hero_cta_url', models.URLField(help_text='Hero CTA Text', max_length=255)),
                ('event', wagtail.core.fields.StreamField((('row', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('datetime_google', wagtail.core.blocks.CharBlock()), ('datetime_reader', wagtail.core.blocks.CharBlock()), ('location_up', wagtail.core.blocks.CharBlock()), ('location_down', wagtail.core.blocks.CharBlock()), ('eventbrite', wagtail.core.blocks.URLBlock()), ('googlemap', wagtail.core.blocks.URLBlock()), ('description', wagtail.core.blocks.RichTextBlock())))),), blank=True, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
