from django.db import models


class AvailableObjectsManager(models.Manager):
    """
    Менеджер для работы только "не удаленными объектами" и не активных.
    """
    def get_queryset(self):
        return super().get_queryset().exclude(is_deleted=True, is_active=False)
