from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.TextField(verbose_name='title', max_length=100)
    category = models.TextField(verbose_name='category', max_length=100, blank=True)
    text = models.TextField(verbose_name='text', max_length=1000)
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)

    def __str__(self):
        return self. title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'
