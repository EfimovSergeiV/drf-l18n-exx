from django.db import models
from parler.models import TranslatableModel, TranslatedFields





class NewsModel(TranslatableModel):
    """ Модель новости """

    title = models.CharField(verbose_name="Заголовок", max_length=255)

    translations = TranslatedFields(
        text = models.CharField(verbose_name="Текст", max_length=200)
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title