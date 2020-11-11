# Generated by Django 3.0.7 on 2020-07-12 23:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200712_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('category', models.PositiveIntegerField(choices=[(0, 'awards'), (1, 'career'), (2, 'volunteer'), (3, 'physics')], default=1)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='studentday',
            old_name='image1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='townhall',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='studentday',
            name='file1',
        ),
        migrations.RemoveField(
            model_name='studentday',
            name='file2',
        ),
        migrations.RemoveField(
            model_name='studentday',
            name='file3',
        ),
        migrations.RemoveField(
            model_name='studentday',
            name='file4',
        ),
        migrations.RemoveField(
            model_name='studentday',
            name='file5',
        ),
        migrations.RemoveField(
            model_name='studentday',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='townhall',
            name='file1',
        ),
        migrations.RemoveField(
            model_name='townhall',
            name='file2',
        ),
        migrations.RemoveField(
            model_name='townhall',
            name='file3',
        ),
        migrations.RemoveField(
            model_name='townhall',
            name='file4',
        ),
        migrations.RemoveField(
            model_name='townhall',
            name='file5',
        ),
        migrations.RemoveField(
            model_name='townhall',
            name='image2',
        ),
        migrations.CreateModel(
            name='ResourcePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('aboutblock', ckeditor.fields.RichTextField()),
                ('awardblock', ckeditor.fields.RichTextField()),
                ('volunteerblock', ckeditor.fields.RichTextField()),
                ('careerblock', ckeditor.fields.RichTextField()),
                ('last_modified', models.DateField(auto_now=True)),
                ('resources', models.ManyToManyField(to='main.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='panel',
            name='resources',
            field=models.ManyToManyField(to='main.Resource'),
        ),
        migrations.AddField(
            model_name='person',
            name='resources',
            field=models.ManyToManyField(to='main.Resource'),
        ),
        migrations.AddField(
            model_name='studentday',
            name='resources',
            field=models.ManyToManyField(to='main.Resource'),
        ),
        migrations.AddField(
            model_name='townhall',
            name='resources',
            field=models.ManyToManyField(to='main.Resource'),
        ),
    ]