from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.base.api.views.student import StudentViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r"students", StudentViewSet, basename="student")

api_urls = router.urls