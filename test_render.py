import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capersmed.settings')
django.setup()

from django.test.client import RequestFactory
from core.views import home, products

factory = RequestFactory()
request = factory.get('/')
response = home(request)
content = response.content.decode('utf-8')

if "product-card" in content:
    print("SUCCESS: home.html contains product cards!")
else:
    print("FAIL: home.html does not contain product cards!")
    if "No featured products available." in content:
        print("Reason: No featured products available message is present.")

request = factory.get('/products/')
response = products(request)
content = response.content.decode('utf-8')

if "product-card" in content:
    print("SUCCESS: products.html contains product cards!")
else:
    print("FAIL: products.html does not contain product cards!")
