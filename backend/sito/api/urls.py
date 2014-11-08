from rest_framework import routers
from posti import PostiView
from aule import AuleView
from stabili import StabiliView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'posti', PostiView)
router.register(r'aule', AuleView)
router.register(r'stabili', StabiliView)
urlpatterns = router.urls