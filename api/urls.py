from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from api.views import FixViewSet

router = routers.DefaultRouter()
router.register('fixes', FixViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
