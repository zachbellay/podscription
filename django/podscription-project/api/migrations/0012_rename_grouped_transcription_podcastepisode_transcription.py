# Generated by Django 4.1.3 on 2022-12-25 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_podcastepisode_transcription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcastepisode',
            old_name='grouped_transcription',
            new_name='transcription',
        ),
    ]
