from django.db import models
from authentication.models import User
from advert.models import Advert


class Like(models.Model):
    user_id = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    ad_id = models.ForeignKey(Advert, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
