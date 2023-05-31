from django.urls import path

from .views import ProductCreateListView, ProductDeleteView, PlaybillCreateListView, PlaybillDeleteView

urlpatterns = [
    #### Продукт
    path('product/', ProductCreateListView.as_view()),
    path('product/<int:pk>', ProductDeleteView.as_view()),
    ######   Афиша
    path('playbill/', PlaybillCreateListView.as_view()),
    path('playbill/<int:pk>', PlaybillDeleteView.as_view()),
]