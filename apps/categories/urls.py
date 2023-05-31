from django.urls import path

from .views import CategoryRetrieve, CategoryList


urlpatterns = [
    # Категория
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryRetrieve.as_view()),
]