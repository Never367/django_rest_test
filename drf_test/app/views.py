import rest_framework
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReviewsSerializer
from .models import Products


class ProductsAPIView(generics.ListAPIView, ListModelMixin):
    serializer_class = ReviewsSerializer

    def get_queryset(self) -> QuerySet:
        # Override get_queryset to add additional data to pagination
        pk = self.kwargs['pk']
        product = Products.objects.get(pk=pk)
        queryset = product.reviews.all()
        return queryset

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_cookie)
    def list(
            self,
            request: rest_framework.request.Request,
            *args,
            **kwargs
    ) -> Response:
        # Page caching and data output on request
        response = super().list(request, args, kwargs)
        pk = kwargs.get('pk', None)

        if pk is not None:
            product = Products.objects.get(pk=pk)
            response.data['title'] = product.title
            response.data['asin'] = product.asin
        return response


class ReviewsAPIView(APIView):
    @staticmethod
    def post(
            request: rest_framework.request.Request,
            **kwargs
    ) -> Response:
        # Change of reviews by post request
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Not find pk in request'})

        copy_data = request.data.copy()
        copy_data['asin'] = pk

        serializer = ReviewsSerializer(data=copy_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('The review has been successfully created.')
