# Generated by Django 4.1.3 on 2022-12-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_enable_postgres_trigram'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='podcast',
            name='logo_url',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='podcast',
            name='website_url',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
    ]
