from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register( r'snippets', views.SnippetViewSet )
router.register( r'users', views.UserViewSet )

urlpatterns = [
    path( '', include( router.urls ) ),
]
