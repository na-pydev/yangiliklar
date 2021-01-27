from django.urls import path
from . import views

app_name = "xabar"

urlpatterns = [
    path('', views.bosh_sahifa, name='bosh_sahifa'),
    path('toifa/<toifa>/', views.toifa, name='toifa'),
    path('<xabar_id>/', views.info, name="info"),
    path('ob-havo', views.ob_havo, name='ob-havo' )
]