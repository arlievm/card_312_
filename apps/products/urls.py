from django.urls import path

from .views import ProductCreateListView, ProductDeleteView, PlaybillCreateListView, PlaybillDeleteView, AfishasliderCreateListView, AfishasliderDeteleView, DiscountsliderCreateListView, DiscountsliderDeteleView

urlpatterns = [
    #### Продукт
    path('product/', ProductCreateListView.as_view()),
    path('product/<int:pk>', ProductDeleteView.as_view()),
    ######   Афиша
    path('playbill/', PlaybillCreateListView.as_view()),
    path('playbill/<int:pk>', PlaybillDeleteView.as_view()),
    
    path('Afishaslider/', AfishasliderCreateListView.as_view()),
    path('Afishaslider/<int:pk>', AfishasliderDeteleView.as_view()),
    
    path('Discountslider/', DiscountsliderCreateListView.as_view()),
    path('Discountslider/<int:pk>', DiscountsliderDeteleView.as_view()),
]