# Generated by Django 4.1.3 on 2022-12-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_podcastepisode_whisper_model_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastepisode',
            name='resolved_audio_url',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
    ]