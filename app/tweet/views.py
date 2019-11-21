import os
import logging
import common.message_en as msg
from app.user.backends import JSONWebTokenAuthentication
from app.user.models import User
from app.tweet.models import Tweet
from common.util.response import response
from common.message_en import (
    INVALID_CREDENTIAL, USER_LOGIN_SUCCESS, USER_LOGOUT_SUCCESS, DATA_FETCHED)

from app.user.serializers import (
    SystemUserLoginSerializer,
)
from app.tweet.serializers import (
    TweetListSerializer,
    TweetDetailSerializer,
)

from django.contrib.auth import authenticate
from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from decouple import config

# Setting logger
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def tweet_list(request):
    try:
        user_obj = User.objects.get(email=request.user)
    except Exception as e:
        return response(message=msg.NOT_FOUND, status=404)

    if request.method == 'GET':
        data = []
        serializer = TweetListSerializer(
            Tweet.objects.filter(tweet__isnull=True, user_id=user_obj.id),
            many=True)
        data = serializer.data

        return response(
            data=data,
            message=msg.DATA_FETCHED,
            status=200
        )


@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def tweet_details(request, pk):
    user_obj = request.user
    try:
        user_obj = User.objects.get(email=request.user)
    except Exception as e:
        return response(message=msg.NOT_FOUND, status=404)

    if request.method == 'GET':
        data = []
        try:
            tweet = Tweet.objects.get(id=pk, user_id=user_obj.id)
        except Exception as e:
            return response(message=msg.NOT_FOUND, status=404)
        serializer = TweetDetailSerializer(tweet)
        data = serializer.data

        return response(
            data=data,
            message=msg.DATA_FETCHED,
            status=200
        )
