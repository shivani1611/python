#!/usr/bin/env python

from boto.s3.connection import Location
from boto.s3.connection import S3Connection
from boto.s3.key import Key


from os import environ


def s3_connect(id=None, secret=None):

    # establish connection
    conn = S3Connection(environ.get('PERSONAL_AWS_ACCESS_KEY_ID'),
                        environ.get('PERSONAL_AWS_SECRET_KEY'))

    return conn


def s3_display_all_locations():

    print '\n'.join(i for i in dir(Location) if i[0].isupper())


def s3_create_bucket(conn, bucket_name):

    # create the bucket
    bucket = conn.create_bucket(bucket_name)

    return bucket


def s3_create_bucket_in_region(conn, bucket_name, region):

    # create the bucket in the specified location
    bucket = conn.create_bucket(bucket_name, location=region)

    return bucket


def s3_upload_object(conn, bucket_name, obj_name):

    k = Key(bucket_name)
    k.key = obj_name
    k.set_contents_from_filename(obj_name)

    return k


def s3_create_object(conn, bucket_name, obj_name, body):

    # create a new key object
    k = Key(bucket_name)

    # name the object
    k.key = obj_name

    # populate the content of the object
    k.set_contents_from_string(body)

    return k
