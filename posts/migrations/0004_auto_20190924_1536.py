# Generated by Django 2.2.5 on 2019-09-24 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190923_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Category'),
        ),
    ]
