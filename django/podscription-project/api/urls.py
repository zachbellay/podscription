
from ninja import NinjaAPI

from django.conf import settings
from django.urls import path

# from .views import api
# from .views_internal import api as api_internal
from .views import router as api_router
from .views_internal import router as api_internal_router

if settings.DEBUG:
    api = NinjaAPI()
else:
    api = NinjaAPI(openapi_url=None)

api.add_router('', api_router)
api.add_router('internal/', api_internal_router)

urlpatterns = [
    path("v1/", api.urls),
]
