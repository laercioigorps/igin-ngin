from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from appliances.models import Brand
from appliances.serializers import BrandSerializer
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
