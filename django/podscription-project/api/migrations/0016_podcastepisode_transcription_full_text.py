# Generated by Django 4.1.3 on 2022-12-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_podcastepisode_resolved_audio_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastepisode',
            name='transcription_full_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]