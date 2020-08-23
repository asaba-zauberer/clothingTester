# Generated by Django 3.1 on 2020-08-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_auto_20200822_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='storename',
            field=models.CharField(default=0, max_length=255, verbose_name='店名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='storeurl',
            field=models.CharField(default=1, max_length=1028, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.PositiveIntegerField(choices=[(1, 'tops'), (2, 'bottoms')], verbose_name='カテゴリ'),
        ),
    ]
