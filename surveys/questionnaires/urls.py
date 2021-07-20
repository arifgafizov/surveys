from rest_framework.routers import DefaultRouter

from .views import CreateQuestionnaireViewSet, TakePollViewSet, RetrieveUserQuestionnaireViewSet
router = DefaultRouter()
router.register('questionnaires', CreateQuestionnaireViewSet, basename='questionnaires')
router.register('take-polls', TakePollViewSet, basename='take-polls')
router.register('questionnaires', RetrieveUserQuestionnaireViewSet, basename='questionnaires')
urlpatterns = router.urls