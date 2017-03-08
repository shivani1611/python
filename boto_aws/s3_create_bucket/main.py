#!/usr/bin/env python

# import the aws modules
from boto.s3.connection import S3Connection
from os import environ

# establish the connection
conn = S3Connection(environ.get('PERSONAL_AWS_ACCESS_KEY_ID'),
                    environ.get('PERSONAL_AWS_SECRET_KEY'))
# create the bucket
bucket = conn.create_bucket('aws-random-string-19283334-test1')
