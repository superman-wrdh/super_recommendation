# Generated by Django 2.0.4 on 2019-03-13 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'musician',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('mime_type', models.CharField(max_length=64)),
                ('reference_id', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=255)),
                ('original_file_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('extension', models.CharField(max_length=30)),
                ('storage_type', models.CharField(max_length=30)),
                ('storage_param', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('is_public', models.BooleanField()),
                ('created_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.Musician'),
        ),
    ]