import os
import logging
import common.message_en as msg

from django.contrib.auth import authenticate

from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.settings import api_settings

from app.user.backends import JSONWebTokenAuthentication
from common.util.response import response
from common.message_en import (
    INVALID_CREDENTIAL, USER_LOGIN_SUCCESS, USER_LOGOUT_SUCCESS, DATA_FETCHED)

from app.user.serializers import (
    SystemUserLoginSerializer,
)
from decouple import config

# Setting logger
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

# Create your views here.
@api_view(['POST'])
def user_login(request):
    serializer = SystemUserLoginSerializer(data=request.data)
    if not serializer.is_valid():
        return response(
            data=serializer.errors,
            message=INVALID_CREDENTIAL,
            status=400
        )
    user = authenticate(
        request=request,
        email=serializer.validated_data.get('email'),
        password=serializer.validated_data.get('password')
    )
    
    if not user:
        return response(
            data=serializer.errors,
            message=INVALID_CREDENTIAL,
            status=400
        )
    token = jwt_encode_handler(
        {
            **jwt_payload_handler(user),
        }
    )

    local_response = response(
        data={
            "id": user.id,
            "email": user.email,
            "token": token
        },
        message=USER_LOGIN_SUCCESS,
        status=200
    )
    local_response.set_cookie(
        api_settings.JWT_AUTH_COOKIE,
        token,
        max_age=api_settings.JWT_EXPIRATION_DELTA.total_seconds())
    return local_response


@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def user_logout(request):
    local_response = response(
        message=USER_LOGOUT_SUCCESS,
        status=200
    )
    local_response.delete_cookie(api_settings.JWT_AUTH_COOKIE)
    return local_response


@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def user_details(request):
    user_obj = request.user
    return response(
        data={
            "id": user_obj.id,
            "email": user_obj.email
        },
        message=DATA_FETCHED,
        status=200
    )