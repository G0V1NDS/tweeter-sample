from rest_framework import status
from rest_framework.response import Response
from common.message_en import (SUCCESS, INVALID_DATA)


def return_error_response(msg, code=400, data=None):
    return Response(
        {
            "message": msg,
            "code": code,
            "status": code,
            "success": False,
            "data": data
        },
        status=code
    )


def response(status=status.HTTP_200_OK, message=SUCCESS, data=None, extra={}):
    response_data = {
        "status": status,
        "message": message,
        **extra
    }
    if data is not None:
        response_data['data'] = data
    return Response(
        response_data, status=status
    )


def error_400_409(status=status.HTTP_400_BAD_REQUEST, message=INVALID_DATA, data=[]):
    return response(status=status, message=message, data=data)


def error_common(status=status.HTTP_404_NOT_FOUND, message=INVALID_DATA, data=None):
    return response(status=status, message=message, data=data)


def success_response(status=status.HTTP_200_OK, message=SUCCESS, data=None):
    return response(status=status, message=message, data=data)
