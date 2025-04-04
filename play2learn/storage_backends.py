from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """ Class for storing static files. """
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = True

    def __init__(self, *args, **kwargs):
        print("🚀 Using StaticStorage (S3) for static files!")
        super().__init__(*args, **kwargs)

class PublicMediaStorage(S3Boto3Storage):
    """ Class for storing public media files. """
    location = 'media/public'
    default_acl = 'public-read'
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    location = 'media/private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False