# Generated by Django 5.1.2 on 2024-10-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='average_rating',
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.FileField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(default=0, help_text='Runtime in minutes'),
        ),
        migrations.AddField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
