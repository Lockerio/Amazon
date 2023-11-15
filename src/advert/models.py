from django.core.validators import MinValueValidator
from django.db import models
from authentication.models import User
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Advert(models.Model):
    title = models.CharField(max_length=30)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    cost = models.IntegerField(validators=[MinValueValidator(0)])
    placement_date = models.DateTimeField(editable=False, default=timezone.now())
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title
