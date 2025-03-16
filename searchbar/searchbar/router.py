from searchbarAPP.viewset import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Movie', MovieViewSet, basename='movie')
