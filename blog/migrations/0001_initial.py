# Generated by Django 2.0.4 on 2019-03-13 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('key_world', models.CharField(max_length=128)),
                ('summary', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bloger',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SearchWorld',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogType'),
        ),
        migrations.AddField(
            model_name='blog',
            name='bloger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Bloger'),
        ),
    ]
