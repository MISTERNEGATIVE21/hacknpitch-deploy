# Generated by Django 3.2.7 on 2021-09-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_issue_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
