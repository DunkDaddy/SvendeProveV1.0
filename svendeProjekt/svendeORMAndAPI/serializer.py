from rest_framework import serializers
from .models import *


class BrugerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bruger
        fields = '__all__'


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'


class SubscribedKategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribed_kategori
        fields = '__all__'


class BillederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billeder
        fields = '__all__'


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bruger
        fields = ('brugernavn', 'password')


class BrugernavnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bruger
        fields = ('brugernavn',)
