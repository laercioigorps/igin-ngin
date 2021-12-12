from django.test import TestCase
from appliances.models import Brand
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User


class BrandViewTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            'root1', 'email1@exemple.com', 'root')

        self.brand1 = Brand.objects.create(name="Brastemp")
        self.brand2 = Brand.objects.create(name="Electrolux")
        self.brand3 = Brand.objects.create(name="Continental")

    def test_brand_create(self):
        count = Brand.objects.all().count()
        self.assertEqual(count, 3)

        client = APIClient()
        client.force_authenticate(user=self.user1)
        response = client.post(reverse('appliances:brand_list'),
                               {
            'name': 'LG'
        }, format='json')
        self.assertEqual(response.status_code, 201)

        count = Brand.objects.all().count()
        self.assertEqual(count, 4)

        brand = Brand.objects.get(id=4)
        self.assertEqual(brand.name, 'LG')
