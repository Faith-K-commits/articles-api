from .models import Tag, Article
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
        
class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.CharField()
    
    class Meta:
        model = Article
        fields = ['title', 'description', 'programming_language', 'tags']
        
    def create(self, validated_data):
        # Extract the tags field from validated_data
        tags_data = validated_data.pop('tags')
        
        # Split the comma-separated string into a list of tag names
        tags_list = [tag.strip() for tag in tags_data.split(',')]
        
        # Create the Article object with the remaining validated data
        article = Article.objects.create(**validated_data)
        
        # Create or get Tag objects and associate them with the Article
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