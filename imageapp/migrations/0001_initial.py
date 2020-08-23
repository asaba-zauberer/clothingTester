# Generated by Django 3.1 on 2020-08-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('category', models.PositiveIntegerField(choices=[(1, 'tops'), (2, 'bottoms')], verbose_name='カテゴリ')),
                ('image', models.FileField(upload_to='', verbose_name='画像')),
                ('color', models.PositiveIntegerField(choices=[(1, 'black'), (2, 'white'), (3, 'blue'), (4, 'yellow'), (5, 'else')], verbose_name='色')),
                ('posession', models.BooleanField(verbose_name='所有')),
                ('shopname', models.CharField(max_length=255, null=True, verbose_name='店名')),
                ('shopurl', models.CharField(max_length=1028, null=True, verbose_name='URL')),
            ],
        ),
    ]
