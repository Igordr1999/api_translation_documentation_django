from rest_framework import serializers
from news.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('section', 'title', 'rating', 'text', 'title_ru', 'title_en', 'title_de')
