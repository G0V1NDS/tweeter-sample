import os
import logging
import uuid
import re

from django.conf import settings
from django.core.signing import TimestampSigner

from common.constants import EMAIL_REGEX


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def get_time_stamp_signer():
    return TimestampSigner()


def represent_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def generate_confirmation_token(email):
    signer = get_time_stamp_signer()
    value = signer.sign(email)
    return value


def confirm_token(token, expiration=settings.EMAIL_LINK_EXPIRE_TIME):
    signer = get_time_stamp_signer()
    try:
        email = signer.unsign(token, max_age=expiration)
    except:
        return False

    return email


def generate_html_message_body(subject, message_body):
    message_object = {
        "Subject": {
            "Data": subject
        },
        "Body": {
            "Html": {
                "Data": message_body
            }
        }
    }
    return message_object


def get_unique_name():
    return uuid.uuid4().hex


def get_file_extension(filename):
    filename, file_extension = os.path.splitext(filename)
    return file_extension


def validate_foreign_key(model, fk):
    try:
        model.objects.get(id=fk)
        return fk
    except Exception:
        from rest_framework import serializers
        raise serializers.ValidationError(F"{model.__name__} doesn't exist")


def is_email_valid(email):
    return bool(email and re.match(EMAIL_REGEX, email))

def check_dirs(_path, mode=0o777, exist_ok=True):
    if not os.path.exists(_path):
        os.makedirs(_path, mode=mode, exist_ok=exist_ok)
