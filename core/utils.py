import os

from time import time
from django.core.exceptions import ImproperlyConfigured

LAST_TIMESTAMP = 0


def timestamp_seconds():
    global LAST_TIMESTAMP

    timestamp = int(time())
    LAST_TIMESTAMP = (LAST_TIMESTAMP + 1) if timestamp <= LAST_TIMESTAMP else timestamp

    return LAST_TIMESTAMP


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


def logo_location(instance, filename):
    return "%s/%s/%s" % (instance.name, "logo", filename)


def banner_location(instance, filename):
    return "%s/%s/%s" % (instance.name, "banner", filename)


def profile_location(instance, filename):
    return "%s/%s" % ( "profile", filename)
