from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from . import views

router = routers.DefaultRouter()
router.register(r'appusers', views.AppUserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi/', get_schema_view(
        title="Tinderlike API",
        description="API for the app that will be an even better success than Tinder"
    ), name='openapi-schema')
]
