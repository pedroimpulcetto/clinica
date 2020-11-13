"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers

from pacientes.api.viewsets import PacientesViewSet
from pacientes.api.viewsets import PacientesDetalhesViewSet
from agendamentos.api.viewsets import AgendamentosViewSet
from horarios.api.viewsets import HorariosViewSet
from historicos.api.viewsets import HistoricosViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacientesViewSet)
# router.register(r'detalhes', PacientesDetalhesViewSet)
router.register(r'agendamentos', AgendamentosViewSet)
router.register(r'horarios', HorariosViewSet)
router.register(r'historicos', HistoricosViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
