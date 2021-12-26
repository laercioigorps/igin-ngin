from django.test import TestCase
from profiles.models import Organization, Profile, Customer, OrganizationAdress, UserAdress
from django.contrib.auth.models import User
from datetime import date

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


class ProfileModelTest(TestCase):
    def setUp(self):
        # initiate user
        self.user1 = User.objects.create_user(
            'root1', 'email1@exemple.com', 'root')
        self.user2 = User.objects.create_user(
            'root2', 'email2@exemple.com', 'root')
        self.user3 = User.objects.create_user(
            'root3', 'email3@exemple.com', 'root')

        self.org1 = Organization.objects.create(name="Eletro service")
        self.org2 = Organization.objects.create(name="Conservice")

    def test_create_user_profile(self):
        # count profile objects and assert = 3
        profileCount = Profile.objects.all().count()
        self.assertEquals(profileCount, 3)
        # create new user and test if there is new profile
        self.user4 = User.objects.create_user(
            'root4', 'email4@exemple.com', 'root')
        profileCount2 = Profile.objects.all().count()
        self.assertEquals(profileCount+1, profileCount2)

    def test_update_user_profile(self):
        self.user3.profile.bio = "added a bio"
        self.user3.profile.org = self.org1
        self.user3.first_name = "joao"
        self.user3.profile.birth_date = date.today()
        self.user3.save()

        user = User.objects.get(pk=self.user3.id)
        self.assertEquals(user.profile.bio, "added a bio")
        self.assertEquals(user.profile.org, self.org1)
        self.assertEquals(user.first_name, "joao")
        self.assertEquals(user.profile.birth_date, date.today())


class CustomerModelTest(TestCase):

    def setUp(self):
        # initiate user
        self.user1 = User.objects.create_user(
            'root1', 'email1@exemple.com', 'root')
        self.user2 = User.objects.create_user(
            'root2', 'email2@exemple.com', 'root')
        self.user3 = User.objects.create_user(
            'root3', 'email3@exemple.com', 'root')
        # initiate organizations
        self.org1 = Organization.objects.create(name="Eletro service")
        self.org2 = Organization.objects.create(name="Conservice")
        # initiate customers
        self.customer1 = Customer.objects.create(
            name="Jake", created_by=self.user1, org=self.org1)
        self.customer2 = Customer.objects.create(
            name="Maria", created_by=self.user2, org=self.org2)
        self.customer3 = Customer.objects.create(
            name="Carlos", created_by=self.user2, org=self.org2)

    def test_create_customer(self):
        countCustomer = Customer.objects.all().count()
        self.assertEquals(countCustomer, 3)
        customer = Customer.objects.create(
            name="Jake", created_by=self.user1, org=self.org1)
        countCustomer = Customer.objects.all().count()
        self.assertEquals(countCustomer, 4)
        self.assertEquals(customer.name, "Jake")
        self.assertEquals(customer.created_by, self.user1)
        self.assertEquals(customer.org, self.org1)
        self.assertEquals(customer.created_on, date.today())
        self.assertEquals(customer.is_active, True)

    def test_update_customer(self):
        self.customer3.nickName = "Carlinho"
        self.customer3.indication = self.customer2
        self.customer3.email = "Carlinho@hotmail.com"
        self.customer3.fone = "91980808080"
        self.customer3.profession = "Lawyer"
        self.customer3.birth_date = date(year=1997, month=8, day=9)
        self.customer3.save()

        customer = Customer.objects.get(pk=self.customer3.id)
        self.assertEquals(customer.nickName, 'Carlinho')
        self.assertEquals(customer.indication, self.customer2)
        self.assertEquals(customer.email, "Carlinho@hotmail.com")
        self.assertEquals(customer.fone, '91980808080')
        self.assertEquals(customer.profession, 'Lawyer')
        self.assertEquals(customer.birth_date, date(year=1997, month=8, day=9))


class OrganizationAdressTest(TestCase):
    def setUp(self):
        # initiate organizations
        self.org1 = Organization.objects.create(name="Eletro service")
        self.org2 = Organization.objects.create(name="Conservice")

    def test_create_adress_and_associate_with_organization(self):
        orgAdressCount = OrganizationAdress.objects.all().count()
        self.assertEquals(orgAdressCount, 0)
        OrganizationAdress.objects.create(
            street="alameda José Maria Esp", neighborhood="Cariri",
            city="Castanhal", number="5", owner=self.org1)
        orgAdressCount = OrganizationAdress.objects.all().count()
        self.assertEquals(orgAdressCount, 1)

    def test_create_multiple_adress_and_associate_with_organization(self):
        orgAdressCount = OrganizationAdress.objects.all().count()
        self.assertEquals(orgAdressCount, 0)
        OrganizationAdress.objects.create(
            street="alameda José Maria Esp", neighborhood="Cariri",
            city="Castanhal", number="5", owner=self.org1)
        orgAdressCount = OrganizationAdress.objects.all().count()
        self.assertEquals(orgAdressCount, 1)

        OrganizationAdress.objects.create(
            street="alameda Imperial", neighborhood="São josé",
            city="Castanhal", number="50", owner=self.org1)

        orgAdressCount = self.org1.organizationadress_set.all().count()
        self.assertEquals(orgAdressCount, 2)


class UserAdressTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            'root1', 'email1@exemple.com', 'root')
        self.user2 = User.objects.create_user(
            'root2', 'email2@exemple.com', 'root')
        self.user3 = User.objects.create_user(
            'root3', 'email3@exemple.com', 'root')

    def test_create_adress_and_associate_with_organization(self):
        userAdressCount = UserAdress.objects.all().count()
        self.assertEquals(userAdressCount, 0)
        UserAdress.objects.create(
            street="alameda José Maria Esp", neighborhood="Cariri",
            city="Castanhal", number="5", owner=self.user1)
        userAdressCount = self.user1.useradress_set.all().count()
        self.assertEquals(userAdressCount, 1)

    def test_create_multiple_adress_and_associate_with_user(self):
        userAdressCount = UserAdress.objects.all().count()
        self.assertEquals(userAdressCount, 0)
        UserAdress.objects.create(
            street="alameda José Maria Esp", neighborhood="Cariri",
            city="Castanhal", number="5", owner=self.user1)
        userAdressCount = self.user1.useradress_set.all().count()
        self.assertEquals(userAdressCount, 1)

        UserAdress.objects.create(
            street="alameda Imperial", neighborhood="São josé",
            city="Castanhal", number="50", owner=self.user1)

        userAdressCount = self.user1.useradress_set.all().count()
        self.assertEquals(userAdressCount, 2)
