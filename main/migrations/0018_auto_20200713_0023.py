# Generated by Django 3.0.7 on 2020-07-13 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200713_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='resources',
            field=models.ManyToManyField(blank=True, to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='person',
            name='resources',
            field=models.ManyToManyField(blank=True, to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='resources',
            field=models.ManyToManyField(blank=True, to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='studentday',
            name='resources',
            field=models.ManyToManyField(blank=True, to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='townhall',
            name='resources',
            field=models.ManyToManyField(blank=True, to='main.Resource'),
        ),
    ]