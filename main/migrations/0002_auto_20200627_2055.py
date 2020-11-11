# Generated by Django 3.0.7 on 2020-06-27 20:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('website', models.URLField(blank=True, null=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('zipcode', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='summary',
            new_name='description',
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='TownHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('block0', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('block1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file1', models.FileField(blank=True, null=True, upload_to='')),
                ('file2', models.FileField(blank=True, null=True, upload_to='')),
                ('file3', models.FileField(blank=True, null=True, upload_to='')),
                ('file4', models.FileField(blank=True, null=True, upload_to='')),
                ('file5', models.FileField(blank=True, null=True, upload_to='')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('last_modified', models.DateField(auto_now=True)),
                ('conference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Conference')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Location')),
                ('panel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('block0', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('block1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file1', models.FileField(blank=True, null=True, upload_to='')),
                ('file2', models.FileField(blank=True, null=True, upload_to='')),
                ('file3', models.FileField(blank=True, null=True, upload_to='')),
                ('file4', models.FileField(blank=True, null=True, upload_to='')),
                ('file5', models.FileField(blank=True, null=True, upload_to='')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('last_modified', models.DateField(auto_now=True)),
                ('conference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Conference')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Location')),
            ],
        ),
        migrations.AddField(
            model_name='panel',
            name='people',
            field=models.ManyToManyField(blank=True, null=True, to='main.Person'),
        ),
        migrations.AddField(
            model_name='conference',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Location'),
        ),
    ]