from django.urls import path
from .views import ProductsAPIView, ReviewsAPIView


# url for api
urlpatterns = [
    path('products/<int:pk>/', ProductsAPIView.as_view()),
    path('create_review_for_product/<int:pk>/', ReviewsAPIView.as_view())
]
