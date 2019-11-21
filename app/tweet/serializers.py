from rest_framework import serializers
from app.tweet.models import Tweet


class TweetCreateSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=160)
    user_id = serializers.IntegerField(required=True)
    original_user_id = serializers.IntegerField()
    tweet_id = serializers.IntegerField()

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'user_id', 'original_user_id', 'tweet_id')

    def create(self, validated_data):
        tweet = Tweet.objects.create(**validated_data)
        return tweet

class TweetListSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    original_user_name = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'user_id', 'original_user_id', 'user_name', 'original_user_name')

    def get_user_name(self, obj):
        try:
            return obj.user.name
        except Exception as e:
            return None
    
    def get_original_user_name(self, obj):
        try:
            return obj.original_user.name
        except Exception as e:
            return None

class TweetDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    original_user_name = serializers.SerializerMethodField()
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'user_id', 'original_user_id', 'user_name', 'original_user_name', 'reply', 'is_retweet', 'is_reply')

    def get_user_name(self, obj):
        try:
            return obj.user.name
        except Exception as e:
            return None
    
    def get_original_user_name(self, obj):
        try:
            return obj.original_user.name
        except Exception as e:
            return None
    
    def get_reply(self, obj):
        try:
            replies = Tweet.objects.filter(is_reply=True, tweet_id=obj.id)
            serialized_tweets = TweetListSerializer(replies, many=True)
            return serialized_tweets.data
        except Exception as e:
            return None
    
