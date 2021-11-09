from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField('Tag', through='Relationship')

    class Meta:
        db_table = 'article'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Метка')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

    def __str__(self):
        return self.title


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    isMain = models.BooleanField()



