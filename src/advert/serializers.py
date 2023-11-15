from rest_framework import serializers
from advert.models import Advert, Tag


class AdvertListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='advert-detail')

    class Meta:
        model = Advert
        fields = ["id", "title", "photo", "url", "cost"]


class AdvertDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    tags = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    author_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def is_valid(self, raise_exception=False):
        # If there are no tags in a request, empty list will be substituted as tags
        self._tags = self.initial_data.pop("tags", [])
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        advert = Advert.objects.create(**validated_data)

        for tag in self._tags:
            obj, _ = Tag.objects.get_or_create(name=tag)
            advert.tags.add(obj)

        advert.save()
        return advert

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    tags = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name',
    )

    def is_valid(self, raise_exception=False):
        if 'tags' in self.initial_data:
            self._tags = self.initial_data.pop('tags')
        else:
            self._tags = [tag.name for tag in self.instance.tags.all()]

        super().is_valid(raise_exception=raise_exception)

    def save(self):
        advert = super().save()

        for tag in self._tags:
            obj, _ = Tag.objects.get_or_create(name=tag)
            advert.tags.add(obj)

        advert.save()
        return advert

    class Meta:
        model = Advert
        fields = ["id", "title", "description", "photo", "location", "cost", "tags"]


class AdvertDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ["id"]


if __name__ == '__main__':
    pass
