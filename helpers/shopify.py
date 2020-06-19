import  shopify
from django.conf import settings


class ShopifyClient(object):
    def __init__(self):
        self.setup_client(settings.SHOPIFY_APP_NAME,
                          settings.SHOPIFY_APP_API_KEY,
                          settings.SHOPIFY_PASSWORD,
                          settings.SHOPIFY_API_VERSION,
                          settings.SHOPIFY_SHARED_SECRET,
                          settings.SHOPIFY_STORE_FRONT_ACCESS_TOKEN,
                          scope=settings.SHOPIFY_SCOPE)

    def setup_client(self, SHOP_NAME, API_KEY, PASSWORD, API_VERSION, SHARED_SECRET, ACCESS_TOKEN, scope=[]):
        shop_url_short = "https://%s.myshopify.com" % (SHOP_NAME,)
        shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, SHOP_NAME, API_VERSION)
        shopify.ShopifyResource.set_site(shop_url)
        shopify.Session.setup(api_key=API_KEY, secret=SHARED_SECRET)
        session = shopify.Session(shop_url_short, version=API_VERSION)
        session.token = ACCESS_TOKEN
        shopify.ShopifyResource.activate_session(session)

    def get_products(self, limit, page ):
        return shopify.Product.find(limit=limit, page=page)

    def create_order(self, order_data): # item_id, cost
        return shopify.Order.create(order_data)