# Django
from django.urls import path, include

# rest_framework
from rest_framework.routers import DefaultRouter

# local
from . import controllers

router = DefaultRouter()
router.register(r'', controllers.QuestionController, basename='')

urlpatterns = [
    path('', include(router.urls)),
]