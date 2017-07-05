from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.models import Location, Department, Category, Subcategory, FlatData


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        depth = 2
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = Department
        depth = 2
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        depth = 2
        fields = '__all__'


class SubcategorySerializer(ModelSerializer):

    class Meta:
        model = Subcategory
        depth = 3
        fields = '__all__'


class FlatDataSerializer(ModelSerializer):

    class Meta:
        model = FlatData
        depth = 4
        fields = '__all__'
