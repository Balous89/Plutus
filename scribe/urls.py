from django.urls import path
from . import views

app_name = 'scribe'


urlpatterns = [
    path('transitrouteform/', views.GetTransitPoints.as_view(),
         name='transitrouteform'),
]
