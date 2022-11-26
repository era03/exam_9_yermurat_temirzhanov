from django.db import models
from django.contrib.auth import get_user_model



class Picture(models.Model):
    picture = models.ImageField(
        null=True,
        blank=True,
        upload_to='pictures',
        verbose_name='Фотографии'
    )
    description = models.CharField(
        max_length=300, 
        blank=True, 
        null=True, 
        default=' ', 
        verbose_name='Подпись'
    )
    favorite = models.ManyToManyField(
        to=''
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания', 
        auto_now_add=True
    )
    author = models.ForeignKey(
        to=get_user_model(),
        verbose_name='Автор фотографии',
        related_name='author_picture',
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.description} - {self.author} - {self.author}'