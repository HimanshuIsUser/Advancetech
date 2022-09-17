# Generated by Django 4.0.5 on 2022-08-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=13)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=250)),
                ('Timestamp', models.DateField(blank=True)),
            ],
        ),
    ]