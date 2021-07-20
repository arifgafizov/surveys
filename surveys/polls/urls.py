from rest_framework.routers import DefaultRouter

from .views import PollViewSet, CreateUpdateDestroyPollViewSet

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')
router.register('admin-polls', CreateUpdateDestroyPollViewSet, basename='admin-polls')
urlpatterns = router.urls
