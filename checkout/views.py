from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  helpers.shopify import ShopifyClient


class CreateOrderAPIView(APIView):

    def post(self, request, **kwargs):
        shopify_client = ShopifyClient()
        return shopify_client.create_order(request.data)