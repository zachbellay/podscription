# Generated by Django 4.1.3 on 2023-01-31 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_search_vector_trigger'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='hit_counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
