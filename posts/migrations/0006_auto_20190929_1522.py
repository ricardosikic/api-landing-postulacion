# Generated by Django 2.2.5 on 2019-09-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190924_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
