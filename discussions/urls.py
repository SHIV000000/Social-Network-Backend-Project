from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscussionViewSet, HashtagViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'discussions', DiscussionViewSet)
router.register(r'hashtags', HashtagViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
