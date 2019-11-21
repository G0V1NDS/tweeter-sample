from django.db import models
from app.user.models import User

from common.util.base_model import BaseModelMixin
# Create your models here.


class Tweet(BaseModelMixin):
    content = models.CharField(max_length=160)
    user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    original_user = models.ForeignKey(
        User, related_name="original_user", on_delete=models.CASCADE)
    tweet = models.ForeignKey(
        'self', related_name="tweet_parent", on_delete=models.CASCADE, null=True)
    is_retweet = models.BooleanField(default=False)
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'tweets'

class Likes(BaseModelMixin):
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'likes'
