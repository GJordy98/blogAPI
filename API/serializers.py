from .models import Blog, Category, Commentaires
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'category', 'author', 'date_created', 'date_updated']
        read_only_fields = ['titre', 'contenu', 'author', 'date_created']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created']


class CommentairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaires
        fields = ['id', 'blog', 'author', 'content', 'date_creation']