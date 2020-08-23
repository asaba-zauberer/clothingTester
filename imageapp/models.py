from django.db import models

# Create your models here.
CATEGORY = (
    (1, 'tops'),
    (2, 'bottoms'),
)
COLOR = (
    (1, 'black'),
    (2, 'white'),
    (3, 'blue'),
    (4, 'yellow'),
    (5, 'else'),
)


class Item(models.Model):
    name = models.CharField(verbose_name='名前',max_length=255,null=False)
    category = models.PositiveIntegerField(verbose_name='カテゴリ',choices=CATEGORY)
    image = models.FileField(verbose_name='画像')
    color = models.PositiveIntegerField(verbose_name='色',choices=COLOR)
    posession= models.BooleanField(verbose_name='所有',null=False)
    shopname = models.CharField(verbose_name='店名',max_length=255,null=True)
    shopurl = models.CharField(verbose_name='URL',max_length=1028,null=True)

    def __str__(self):
        return self.name
