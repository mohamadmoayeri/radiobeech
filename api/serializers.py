from rest_framework import serializers

from home.models import story

from profiles.models import personal_information

class personal_information_serializer(serializers.ModelSerializer):

    class Meta:

        model=personal_information

        fields="__all__"


class story_serializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        #many=True,
        read_only=True,
        slug_field='username'
     )

    class Meta:

        model=story
        
        fields="__all__"   