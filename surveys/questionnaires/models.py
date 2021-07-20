from django.db import models
from django.db.models import JSONField
from django.conf import settings

from common.base_model import BaseModel
from polls.models import Poll


class Questionnaire(BaseModel):
    """
    Контейнер структуры анкета
    """
    poll = models.ForeignKey(
        Poll,
        verbose_name="Опрос",
        on_delete=models.PROTECT,
    )
    text = models.CharField(
        'Текст вопроса',
        max_length=1000,
        help_text='Описание',
        blank=True,
        default=''
    )
    answers_data = JSONField("Данные ответов", default=list)
    additional_info = JSONField("Дополнительные информация", default=list, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        related_name="created_%(class)s",
        null=True
    )
