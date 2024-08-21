from .models import Tag, Article
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tags_input = serializers.CharField(write_only=True)

    class Meta:
        model = Article
        fields = ['title', 'description', 'programming_language', 'tags', 'tags_input']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags_input')
        tags_list = [tag.strip() for tag in tags_data.split(',')]
        article = Article.objects.create(**validated_data)

        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            article.tags.add(tag)

        return article

    def validate(self, data):
        errors = []
        for field, value in data.items():
            try:
                self.fields[field].run_validators(value)
            except serializers.ValidationError as e:
                errors.append({'field': field, 'message': str(e)})

        if errors:
            raise serializers.ValidationError({"errors": errors})
        return data