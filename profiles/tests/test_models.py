from django.test import TestCase
from profiles.models import Organization

# Create your tests here.


class OrganizationModelTest(TestCase):

    def setUp(self):
        self.org1 = Organization.objects.create(name="Eletro service")
        self.org2 = Organization.objects.create(name="Conservice")
        self.org3 = Organization.objects.create(name="LaercioMR")

    def test_create_organization(self):
        # count numbers of Organizations object and assert
        orgCount = Organization.objects.all().count()
        self.assertEquals(orgCount, 3)
        # create organization object and assert count increased
        Organization.objects.create(name="Eletro service")
        orgCount2 = Organization.objects.all().count()
        self.assertEquals(orgCount+1, orgCount2)
