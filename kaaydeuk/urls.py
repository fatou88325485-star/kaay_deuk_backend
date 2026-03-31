"""
URL configuration for kaaydeuk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from kaaydeuk.views import (
    api_root,
    UtilisateurViewSet, ChercheurViewSet, AdministrateurViewSet,
    LocataireViewSet, TypeLogementViewSet, LogementViewSet,
    ImageViewSet, Video3DViewSet, FavoriViewSet, ReservationViewSet,
    PaiementViewSet, Visite3DViewSet
)

# Create a router and register viewsets
router = SimpleRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'chercheurs', ChercheurViewSet)
router.register(r'administrateurs', AdministrateurViewSet)
router.register(r'locataires', LocataireViewSet)
router.register(r'types-logement', TypeLogementViewSet)
router.register(r'logements', LogementViewSet)
router.register(r'images', ImageViewSet)
router.register(r'videos-3d', Video3DViewSet)
router.register(r'favoris', FavoriViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'paiements', PaiementViewSet)
router.register(r'visites-3d', Visite3DViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Swagger documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
