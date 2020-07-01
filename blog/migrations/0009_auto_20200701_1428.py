# Generated by Django 3.0.6 on 2020-07-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200619_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title for Your Blog'),
        ),
    ]
