# Generated by Django 3.1.4 on 2020-12-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_holiday_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=100),
            preserve_default=False,
        ),
    ]