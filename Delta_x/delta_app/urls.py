from django.urls import path

from .views import NasaHomeView, DataListView


urlpatterns = [
    path('', NasaHomeView.as_view(), name="nasaHome"),
    path('data/', DataListView.as_view(), name='datalist'),
]
