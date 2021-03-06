# Generated by Django 3.2.4 on 2021-06-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('poster', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=500)),
                ('year', models.PositiveIntegerField()),
                ('movie', models.FileField(upload_to='')),
                ('avg_rate', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('genre', models.ManyToManyField(to='Cinema.Movie')),
            ],
        ),
    ]
