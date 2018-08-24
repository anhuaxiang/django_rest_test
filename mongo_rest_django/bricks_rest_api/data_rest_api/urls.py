from django.conf.urls import url, include
from rest_framework_mongoengine import routers as merouters
from data_rest_api.views import ToolViewSet


merouter = merouters.DefaultRouter()
merouter.register(r'mongo', ToolViewSet)

urlpatterns = [
    url(r'^', include(merouter.urls)),
]

