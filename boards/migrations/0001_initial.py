# Generated by Django 3.0.6 on 2020-06-02 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=140)),
                ('guests', models.IntegerField(help_text='How many people will be staying?')),
                ('beds', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('check_in', models.TimeField()),
                ('check_out', models.TimeField()),
                ('instant_book', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Board Type',
            },
        ),
        migrations.CreateModel(
            name='CoursePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': '수강기간',
            },
        ),
        migrations.CreateModel(
            name='LectureCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': '강의비',
            },
        ),
        migrations.CreateModel(
            name='TeachingTextbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': '강의 교재',
            },
        ),
        migrations.CreateModel(
            name='TextbookFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': '교재 특징',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='board_photos')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='boards.Board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='board',
            name='board_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boards', to='boards.BoardType'),
        ),
        migrations.AddField(
            model_name='board',
            name='course_period',
            field=models.ManyToManyField(blank=True, related_name='boards', to='boards.CoursePeriod'),
        ),
        migrations.AddField(
            model_name='board',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='board',
            name='lecture_cost',
            field=models.ManyToManyField(blank=True, related_name='boards', to='boards.LectureCost'),
        ),
        migrations.AddField(
            model_name='board',
            name='teaching_textbooks',
            field=models.ManyToManyField(blank=True, related_name='boards', to='boards.TeachingTextbooks'),
        ),
    ]
