#!/usr/bin/env python

# import the aws modules
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from os import environ

# establish the connection
conn = S3Connection(environ.get('PERSONAL_AWS_ACCESS_KEY_ID'),
                    environ.get('PERSONAL_AWS_SECRET_KEY'))
# create the bucket
bucket = conn.create_bucket('aws-random-string-19283334-test1')

# create a new key
k = Key(bucket)
k.key = 'foobar'

# populate the content of the key
k.set_contents_from_string('This is a test of S3')
