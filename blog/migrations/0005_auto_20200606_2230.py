# Generated by Django 3.0.6 on 2020-06-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200606_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Username'),
        ),
    ]