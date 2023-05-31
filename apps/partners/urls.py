from django.urls import path

from .views import PartnersCreateListView, PartnersDeleteView


urlpatterns = [
    # Категория
    path('partners/', PartnersCreateListView.as_view()),
    path('partners/<int:pk>', PartnersDeleteView.as_view()),
]