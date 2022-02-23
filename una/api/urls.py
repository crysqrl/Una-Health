from django.urls import include, path
from rest_framework import routers
from una.api import views

router = routers.SimpleRouter()
router.register(r'levels', views.GlucoseDataView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('upload/', views.ImportGlucoseData.as_view(), name='upload-file')
]
