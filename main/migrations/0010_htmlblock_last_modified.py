# Generated by Django 3.0.7 on 2020-07-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200702_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='htmlblock',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
    ]