from django.db import models
from filer.fields.image import FilerImageField

class Book(models.Model):
    title = models.CharField(max_length=200)
    cover = FilerImageField(
        null=True,
        blank=True,
        related_name="book_cover",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title

