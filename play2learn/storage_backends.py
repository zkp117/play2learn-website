from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

class PublicMediaStorage(S3Boto3Storage):
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = 'public-read'

class PrivateMediaStorage(S3Boto3Storage):
    location = settings.PRIVATE_MEDIA_STORAGE
    default_acl = 'private'
    custom_domain = False
