from rest_framework import serializers
from .models import Discussion, Hashtag, Comment

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'discussion', 'author', 'text', 'created_on', 'likes']

class DiscussionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    hashtags = HashtagSerializer(many=True)

    class Meta:
        model = Discussion
        fields = ['id', 'author', 'text', 'image', 'hashtags', 'created_on', 'view_count', 'comments']
