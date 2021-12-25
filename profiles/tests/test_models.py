from django.test import TestCase
from profiles.models import Organization, Profile
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
