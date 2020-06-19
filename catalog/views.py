from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  helpers.shopify import ShopifyClient


class ProductApiView(APIView):

    def get(self, request, **kwargs):
        shopify_client = ShopifyClient()
        limit = self.request.GET.get('limit', 50)
        page = self.request.GET.get('page', 1)

        return Response(shopify_client.get_products(limit, page))