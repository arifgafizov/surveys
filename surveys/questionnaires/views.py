from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from polls.models import Poll
from .models import Questionnaire
from .serializers import QuestionnairesSerializer, TakePollSerializer, QuestionSerializer


class CreateQuestionnaireViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnairesSerializer


class TakePollViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = TakePollSerializer
    queryset = Poll.objects.all()


class RetrieveUserQuestionnaireViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnairesSerializer
    @swagger_auto_schema(
        method='get',
        responses={status.HTTP_200_OK: QuestionnairesSerializer()},
    )
    @action(detail=True, methods=['get'])
    def questionnaires(self, request, pk, *args, **kwargs):
        questionnaires = Questionnaire.objects.filter(user_id=pk)
        return Response(QuestionnairesSerializer(questionnaires).data)
