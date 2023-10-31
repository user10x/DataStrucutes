import boto3
import botocore
import sys
BUCKET_NAME = sys.argv[1]
PREFIX = sys.argv[2]
print(BUCKET_NAME)
s3 = boto3.resource('s3')


def main():
    bucket = s3.Bucket(BUCKET_NAME)
    # versions = bucket.object_versions.filter(Prefix=PREFIX)
    versions = bucket.object_versions.filter()

    i = 0
    for version in versions.all():


        if is_delete_marker(version):
            print(version)
            version.delete()


def is_delete_marker(version):
    try:
        # note head() is faster than get()
        version.head()
        return False
    except botocore.exceptions.ClientError as e:
        if 'x-amz-delete-marker' in e.response['ResponseMetadata']['HTTPHeaders']:
            return True
        # an older version of the key but not a DeleteMarker
        elif '404' == e.response['Error']['Code']:
            return False


if __name__ == '__main__':
    main()
