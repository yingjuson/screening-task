from django.urls import include
from . import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"values", views.ValueView)
router.register(r"principles", views.PrincipleView)

urlpatterns = router.urls
