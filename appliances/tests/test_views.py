from django.test import TestCase
from appliances.models import Brand
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
import io


class BrandViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            'root1', 'email1@exemple.com', 'root')
        self.brand1 = Brand.objects.create(name="Brastemp")
        self.brand2 = Brand.objects.create(name="Electrolux")
        self.brand3 = Brand.objects.create(name="Continental")

    def test_brand_create(self):
        # assert existing brands
        count = Brand.objects.all().count()
        self.assertEqual(count, 3)
        # clientAPI setUp and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # post request and assert it was success
        response = client.post(reverse('appliances:brand_list'),
                               {
            'name': 'LG'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        # assert existing brands increased by one
        count = Brand.objects.all().count()
        self.assertEqual(count, 4)
        # assert brand name is the same as in post request
        brand = Brand.objects.get(id=4)
        self.assertEqual(brand.name, 'LG')

    def test_brand_create_with_not_authenticated_user(self):
        # assert existing brands
        count = Brand.objects.all().count()
        self.assertEqual(count, 3)
        # clientAPI setUp but not authenticated
        client = APIClient()
        # post request and assert it was denied
        response = client.post(reverse('appliances:brand_list'),
                               {
            'name': 'LG'
        }, format='json')
        self.assertEqual(response.status_code, 403)
        # assert existing brands do not increased by one
        count = Brand.objects.all().count()
        self.assertEqual(count, 3)

    def test_brand_list_with_authenticated_user(self):
        # assert existing brands
        brandCount = Brand.objects.all().count()
        self.assertEqual(brandCount, 3)
        # clientAPI setUp and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # client get request and assert it was success
        response = client.get(reverse('appliances:brand_list'), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has len==brandCount
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(len(data), 3)

    def test_brand_list_with_not_authenticated_user(self):

        # assert existing brands
        brandCount = Brand.objects.all().count()
        self.assertEqual(brandCount, 3)
        # clientAPI setUp and don't authenticate
        client = APIClient()
        # client get request and assert it was success
        response = client.get(reverse('appliances:brand_list'), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has len==brandCount
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(len(data), 3)

    def test_brand_retrieve_with_authenticated_user(self):
        # get object instance and change the name
        brand = Brand.objects.get(name="Continental")
        brand.name = "Brasileira"
        # clientAPI setUp and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # get request and assert it was success
        response = client.get(reverse('appliances:brand_detail', kwargs={
                              'pk': brand.id}), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has name changed
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(data['name'], "Continental")

    def test_brand_retrieve_with_not_authenticated_user(self):
        # get object instance and change the name
        brand = Brand.objects.get(name="Continental")
        brand.name = "Brasileira"
        # clientAPI setUp and do not authentication
        client = APIClient()
        # get request and assert it was success
        response = client.get(reverse('appliances:brand_detail', kwargs={
                              'pk': brand.id}), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has name changed
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(data['name'], "Continental")

    def test_brand_retrieve_with_invalid_id(self):
        # clientAPI setUp and do not authentication
        client = APIClient()
        # get request and assert it was success
        response = client.get(reverse('appliances:brand_detail', kwargs={
                              'pk': 200}), format='json')
        self.assertEqual(response.status_code, 404)
