from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from appliances.models import Brand, Category, Appliance
from appliances.serializers import BrandSerializer, CategorySerializer, ApplianceSerializer
import io


def get_json_data(serializerData):
    content = JSONRenderer().render(serializerData)
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)
    return data


class BrandSerializerTest(TestCase):

    def setUp(self):
        self.brand1 = Brand.objects.create(name="Brastemp")
        self.brand2 = Brand.objects.create(name="Consul")
        self.brand3 = Brand.objects.create(name="Electrolux")

    def test_brand_serializer_create(self):
        count = Brand.objects.all().count()
        self.assertEqual(count, 3)

        brand = Brand(name='Continental')
        serializer = BrandSerializer(brand)
        data = get_json_data(serializer.data)

        serializer = BrandSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        count = Brand.objects.all().count()
        self.assertEqual(count, 4)

        getBrand = Brand.objects.get(name='Continental')

        self.assertEqual(getBrand.name, 'Continental')


class CategorySerializerTest(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name="Geladeira")
        self.category2 = Category.objects.create(name="Freezer")
        self.category3 = Category.objects.create(name="Maquina de lavar")

    def test_category_serializer_create(self):
        count = Category.objects.all().count()
        self.assertEqual(count, 3)

        category = Category(name='Microondas')
        serializer = CategorySerializer(category)
        data = get_json_data(serializer.data)

        serializer = CategorySerializer(data=data)
        serializer.is_valid()
        serializer.save()

        count = Category.objects.all().count()
        self.assertEqual(count, 4)

        getCategory = Category.objects.get(pk=4)

        self.assertEqual(getCategory.name, 'Microondas')


class ApplianceSerializerTest(TestCase):

    def setUp(self):
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

    def test_category_serializer_create(self):
        # count the number of appliances and assert
        appliancesCount = Appliance.objects.all().count()
        self.assertEqual(appliancesCount, 3)
        # create a appliacen object and serializer
        appliance = Appliance(model='BWC10ABANA',
                              brand=self.brand1, category=self.category1)
        serializer = ApplianceSerializer(appliance)
        # transform serializer data into json data
        data = get_json_data(serializer.data)
        # from the json data we use in the serializer
        serializer = ApplianceSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        # count the number of appliances and assert
        appliancesCount = Appliance.objects.all().count()
        self.assertEqual(appliancesCount, 4)
        getAppliance = Appliance.objects.get(pk=4)
        self.assertEqual(getAppliance.model, 'BWC10ABANA')
