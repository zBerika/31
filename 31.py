INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'cars',
    'animals',
]

from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.species})"

from rest_framework import serializers
from .models import Car, Animal

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

from rest_framework import viewsets
from .models import Car, Animal
from .serializers import CarSerializer, AnimalSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import CarViewSet
from animals.views import AnimalViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
