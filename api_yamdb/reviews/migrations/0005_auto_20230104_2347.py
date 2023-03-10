# Generated by Django 3.2 on 2023-01-04 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20230104_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='categories', to='reviews.category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='genres', to='reviews.genre'),
        ),
    ]
