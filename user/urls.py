from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register("user", UserViewSet, basename="user")
router.register("profile", ProfileViewSet, basename="profile")

urlpatterns = router.urls

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
