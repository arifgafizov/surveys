from django.db import models
from django.db.models import JSONField
from django.conf import settings

from common.base_model import BaseModel
from .constants import QUESTION_TYPES, TEXT_ANSWER


class Poll(BaseModel):
    """
    Контейнер структуры опроса
    """
    title = models.CharField(
        'Название',
        max_length=300,
        help_text='Название опроса'
    )
    description = models.CharField(
        'Описание',
        max_length=1000,
        help_text='Описание',
        blank=True,
        default=''
    )
    date_start = models.DateTimeField(verbose_name='дата старта', blank=True, null=True)
    date_finish = models.DateTimeField(verbose_name='дата окончания', blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Создана пользователем',
        on_delete=models.SET_NULL,
        related_name="created_%(class)s",
        null=True
    )

class Question(BaseModel):
    text = models.CharField(
        'Текст вопроса',
        max_length=1000,
        help_text='Описание',
        blank=True,
        default=''
    )
    type = models.CharField('Тип вопроса', max_length=100, choices=QUESTION_TYPES, default=TEXT_ANSWER)
    variants = models.JSONField('Список вариантов', blank=True, null=True)
    poll = models.ForeignKey(
        Poll,
        verbose_name="Опрос",
        on_delete=models.PROTECT,
    )
