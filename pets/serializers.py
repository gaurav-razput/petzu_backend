from rest_framework import serializers
from pets.models import Pet


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.CharField()
    breedName = serializers.CharField()
    description = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    color = serializers.CharField()
    weight = serializers.CharField()
    height = serializers.CharField()
    length = serializers.IntegerField()
    sellerId = serializers.IntegerField()
    sellerName = serializers.CharField()
    longDescription = serializers.CharField()
    breedId = serializers.IntegerField()

    def create(self, validated_data):
        # Create and return a new `pet` instance, given the validated data.
        return Pet.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        # Update and return an existing `pet` instance, given the validated data.
        instance.breedName = validated_data.get('breedName',instance.breedName)
        instance.image = validated_data.get('image',instance.image)
        instance.description = validated_data.get('description',instance.description)
        instance.age = validated_data.get('age',instance.age)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.color = validated_data.get('color',instance.color)
        instance.weight = validated_data.get('weight',instance.weight)
        instance.height = validated_data.get('height',instance.height)
        instance.length = validated_data.get('length',instance.length)
        instance.sellerId = validated_data.get('sellerId',instance.sellerId)
        instance.sellerName = validated_data.get('sellerName',instance)
        instance.longDescription = validated_data.get('longDescription',instance.longDescription)
        breedId = validated_data.get('breedId',instance.breedId)
        instance.save()
        return instance
