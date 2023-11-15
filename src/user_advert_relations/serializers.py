from rest_framework import serializers

from advert.models import Advert
from advert.serializers import AdvertListSerializer
from user_advert_relations.models import Like


class LikeSerializer(serializers.ModelSerializer):
    ad = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ["id", "ad"]

    def get_ad(self, obj):
        ad_id = obj.ad_id
        return AdvertListSerializer(ad_id, context=self.context).data


class LikeCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    ad_id = serializers.PrimaryKeyRelatedField(queryset=Advert.objects.all())

    class Meta:
        model = Like
        fields = '__all__'

    def get_user_id(self, obj):
        return self.context['request'].user.id

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user
        return super().create(validated_data)


class LikeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id"]


if __name__ == '__main__':
    pass
