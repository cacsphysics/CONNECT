# Generated by Django 3.0.7 on 2020-07-02 19:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_award_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]