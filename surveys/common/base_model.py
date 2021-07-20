from django.db import models

from surveys.models_manager import AvailableObjectsManager


class BaseModel(models.Model):
    """
    Базовая модель, которая содержит общий набор полей для всех моделей проекта.
    """
    objects = models.Manager()
    existing_objects = AvailableObjectsManager()

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    is_active = models.BooleanField(default=True, verbose_name='активность')
    is_deleted = models.BooleanField(default=False, verbose_name='пометка удаленности')

    class Meta:
        """
        Настройки модели.

        Модель является абстрактной.
        """

        abstract = True
