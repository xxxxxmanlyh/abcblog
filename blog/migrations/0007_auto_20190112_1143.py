# Generated by Django 2.1.5 on 2019-01-12 11:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='公告内容'),
        ),
    ]
