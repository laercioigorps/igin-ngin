from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from appliances.models import Brand, Category
from appliances.serializers import BrandSerializer, CategorySerializer
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
