from rest_framework.routers import DefaultRouter
from estudiantes.api.views import EstudiantesViewSet

router = DefaultRouter()
router.register('estudiantes', EstudiantesViewSet, basename= 'estudiante')

urlpatterns = router.urls

