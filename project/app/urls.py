from rest_framework import routers
from .views import UserViewSet, UserProfViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('users/watchlist', UserProfViewSet)

urlpatterns = router.urls