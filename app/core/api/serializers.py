from rest_framework import serializers

from app.core.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


# def greater_than_200_characters(value):
#     if len(value) > 200:
#         raise serializers.ValidationError("Ensure this field has no more than 200 characters.")


# serializers.Serializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     description = serializers.CharField(validators=[greater_than_200_characters])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     # Object level validation
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Ensure that name and description fields are different.")
#         return data

#     # Field level validation
#     # def validate_name(self, data):
#     #     if len(data["name"]) > 50:
#     #         raise serializers.ValidationError("Ensure this field has no more than 50 characters.")
#     #     return data
