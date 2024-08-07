from rest_framework import serializers
from .models import Articles, Comments

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Articles
    fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comments
    fields = ('__all__')