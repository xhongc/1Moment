# Generated by Django 4.2.19 on 2025-03-16 13:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('file_path', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('thumbnail_path', models.ImageField(blank=True, upload_to='thumbnails/%Y/%m/%d/')),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('taken_time', models.DateTimeField(blank=True, null=True)),
                ('size', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('format', models.CharField(max_length=10)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('favorited_by', models.ManyToManyField(blank=True, related_name='favorite_photos', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='photos', to='photos.tag')),
            ],
            options={
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('photos', models.ManyToManyField(related_name='locations', to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='photos.photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_time'],
                'unique_together': {('photo', 'user')},
            },
        ),
    ]
