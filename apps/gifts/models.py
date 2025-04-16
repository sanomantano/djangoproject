from django.db import models

# Create your models here.

class Feedback(models.Model):
    rate = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'