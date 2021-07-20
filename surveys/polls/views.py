from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from .models import Poll
from .serializers import PollListSerializer, CreateDestroyPollSerializer, UpdatePollSerializer


class PollViewSet(ReadOnlyModelViewSet):
    queryset = Poll.existing_objects.all()
    serializer_class = PollListSerializer


class CreateUpdateDestroyPollViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = UpdatePollSerializer
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        # poll is not deleted and its is_deleted field is assigned True
        instance.is_deleted = True
        instance.save()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateDestroyPollSerializer
        return super().get_serializer_class()
