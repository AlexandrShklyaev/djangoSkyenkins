from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='название')
    description = models.CharField(max_length=2000, verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='category/', verbose_name='превью', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Crib(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='название')
    description = models.CharField(max_length=2000, verbose_name='описание', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'шпора'
        verbose_name_plural = 'шпоры'
        ordering = ('name',)
