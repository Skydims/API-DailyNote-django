
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DailyNoteViewSet

router = DefaultRouter()
router.register(r'dailynotes', DailyNoteViewSet, basename='dailynote')

urlpatterns = router.urls
