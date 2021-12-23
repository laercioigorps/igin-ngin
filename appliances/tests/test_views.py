from django.test import TestCase
from appliances.models import Appliance, Brand, Category
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
        # get object instance
        brand = Brand.objects.get(name="Continental")
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
        # get object instance
        brand = Brand.objects.get(name="Continental")
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
        # clientAPI setUp and do not authenticate
        client = APIClient()
        # get request and assert it was success
        response = client.get(reverse('appliances:brand_detail', kwargs={
                              'pk': 200}), format='json')
        self.assertEqual(response.status_code, 404)


class CategoryViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            'root1', 'email1@exemple.com', 'root')
        self.category1 = Category.objects.create(name="Geladeira")
        self.category2 = Category.objects.create(name="Freezer")
        self.category3 = Category.objects.create(name="Maquina de lavar")

    def test_category_create(self):
        # assert existing brands
        categoryCount = Category.objects.all().count()
        self.assertEqual(categoryCount, 3)
        # clientAPI setUp and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # post request and assert it was success
        response = client.post(reverse('appliances:category_list'),
                               {
            'name': 'Microondas'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        # assert existing brands increased by one
        categoryCount = Category.objects.all().count()
        self.assertEqual(categoryCount, 4)
        # assert brand name is the same as in post request
        category = Category.objects.get(id=4)
        self.assertEqual(category.name, 'Microondas')

    def test_category_create_with_not_authenticated_user(self):
        # assert existing categorys
        count = Category.objects.all().count()
        self.assertEqual(count, 3)
        # clientAPI setUp but not authenticated
        client = APIClient()
        # post request and assert it was denied
        response = client.post(reverse('appliances:category_list'),
                               {
            'name': 'Microondas'
        }, format='json')
        self.assertEqual(response.status_code, 403)
        # assert existing categorys do not increased by one
        count = Category.objects.all().count()
        self.assertEqual(count, 3)

    def test_category_list_with_authenticated_user(self):
        # assert existing categorys
        categoryCount = Category.objects.all().count()
        self.assertEqual(categoryCount, 3)
        # clientAPI setUp and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # client get request and assert it was success
        response = client.get(
            reverse('appliances:category_list'), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has len==categoryCount
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(len(data), 3)

    def test_category_list_with_not_authenticated_user(self):
        # assert existing categorys
        categoryCount = Category.objects.all().count()
        self.assertEqual(categoryCount, 3)
        # clientAPI setUp and don't authenticate
        client = APIClient()
        # client get request and assert it was success
        response = client.get(
            reverse('appliances:category_list'), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has len==categoryCount
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(len(data), 3)

    def test_category_retrieve_with_authenticated_user(self):
        # get object instance
        category = Category.objects.get(name="Geladeira")
        # clientAPI setUp and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # get request and assert it was success
        response = client.get(reverse('appliances:category_detail', kwargs={
                              'pk': category.id}), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has name changed
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(data['name'], "Geladeira")

    def test_category_retrieve_with_not_authenticated_user(self):
        # get object instance
        category = Category.objects.get(name="Geladeira")
        # clientAPI setUp and do not authentication
        client = APIClient()
        # get request and assert it was success
        response = client.get(reverse('appliances:category_detail', kwargs={
                              'pk': category.id}), format='json')
        self.assertEqual(response.status_code, 200)
        # transform response into python data and assert it has name changed
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEqual(data['name'], "Geladeira")

    def test_category_retrieve_with_invalid_id(self):
        # clientAPI setUp and do not authentication
        client = APIClient()
        # get request and assert it was success
        response = client.get(reverse('appliances:category_detail', kwargs={
                              'pk': 200}), format='json')
        self.assertEqual(response.status_code, 404)


class ApplianceViewTest(TestCase):
    def setUp(self):
        # initiate user
        self.user1 = User.objects.create_user(
            'root1', 'email1@exemple.com', 'root')
        # initiate categories
        self.category1 = Category.objects.create(name="Geladeira")
        self.category2 = Category.objects.create(name="Freezer")
        self.category3 = Category.objects.create(name="Maquina de lavar")
        # initiate brands
        self.brand1 = Brand.objects.create(name="Brastemp")
        self.brand2 = Brand.objects.create(name="Electrolux")
        self.brand3 = Brand.objects.create(name="Continental")
        # initiate appliances
        self.appliance1 = Appliance.objects.create(
            model="BWC10ABANA", category=self.category3, brand=self.brand1)
        self.appliance2 = Appliance.objects.create(
            model="RFE39", category=self.category1, brand=self.brand2)
        self.appliance3 = Appliance.objects.create(
            model="DF40X", category=self.category1, brand=self.brand2)

    def test_appliance_create_with_authenticated_user(self):
        # count appliances and assert
        appliancesCount = Appliance.objects.all().count()
        self.assertEquals(appliancesCount, 3)
        # api client and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # create appliance post request
        response = client.post(
            reverse('appliances:appliance_list'),
            {
                'model': 'LT12F',
                'category': self.category1.id,
                'brand': self.brand1.id
            },
            format='json')
        self.assertEquals(response.status_code, 201)
        # count appliances and assert
        appliancesCount = Appliance.objects.all().count()
        self.assertEquals(appliancesCount, 4)
        # search object by model and assert data
        appliance = Appliance.objects.get(model="LT12F")
        self.assertEquals(appliance.category, self.category1)
        self.assertEquals(appliance.brand, self.brand1)

    def test_appliance_create_with_not_authenticated_user(self):
        # count appliances and assert
        appliancesCount = Appliance.objects.all().count()
        self.assertEquals(appliancesCount, 3)
        # api client
        client = APIClient()
        # create appliance post request
        response = client.post(
            reverse('appliances:appliance_list'),
            {
                'model': 'LT12F',
                'category': self.category1.id,
                'brand': self.brand1.id
            },
            format='json')
        self.assertEquals(response.status_code, 403)

    def test_appliance_list_with_authenticated_user(self):
        # count appliances and assert
        appliancesCount = Appliance.objects.all().count()
        self.assertEquals(appliancesCount, 3)
        # api client and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # list appliances get request
        response = client.get(
            reverse('appliances:appliance_list'), format='json')
        self.assertEquals(response.status_code, 405)

    def test_appliance_retrieve_with_authenticated_user(self):
        # api client and authentication
        client = APIClient()
        client.force_authenticate(user=self.user1)
        # get request by id
        response = client.get(
            reverse('appliances:appliance_detail', kwargs={"pk": 1}),
            format='json')
        self.assertEquals(response.status_code, 200)
        # response into python and assert its fields are correct
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        self.assertEquals(data['model'], self.appliance1.model)
        self.assertEquals(data['brand'], self.appliance1.brand.id)
        self.assertEquals(data['category'], self.appliance1.category.id)
