from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=30)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Customer(models.Model):
    name = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    nickName = models.CharField(max_length=30, null=True)
    indication = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    fone = models.CharField(max_length=30, null=True)
    profession = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True)


class Adress(models.Model):
    street = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, default="Brasil")
    coordinates = models.CharField(max_length=30, null=True)
    number = models.CharField(max_length=20)
    complement = models.CharField(max_length=40, null=True)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=30, null=True)

    class Meta:
        abstract = True


class OrganizationAdress(Adress):
    owner = models.ForeignKey(Organization, on_delete=models.CASCADE)


class UserAdress(Adress):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
