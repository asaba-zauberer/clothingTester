# Generated by Django 3.1 on 2020-08-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.PositiveIntegerField(verbose_name='カテゴリ'),
        ),
    ]