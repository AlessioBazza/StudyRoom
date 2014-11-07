from django.conf.urls import patterns, url
from rest_framework import routers
import restful

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'posti', restful.PostiView)
router.register(r'aule', restful.AuleView)
urlpatterns = router.urls