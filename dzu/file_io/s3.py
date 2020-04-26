"""
This module contains utility functions for reading and writing a variety of
objects from and to AWS S3.
"""


import pickle as pkl
from io import StringIO

import boto3
import pandas as pd

from . import check_path


def save_binary_to_s3(obj, bucket, path):
    s3 = boto3.resource('s3')
    path = check_path(path, str)
    s3_obj = s3.Object(bucket, path)
    s3_obj.put(Body=pkl.dumps(obj))


def load_binary_from_s3(bucket, path):
    s3 = boto3.resource('s3')
    path = check_path(path, str)
    s3_obj = s3.Object(bucket, path)
    obj = pkl.loads(s3_obj.get()['Body'].read())
    return obj


def load_text_from_s3(bucket, path):
    s3 = boto3.resource('s3')
    path = check_path(path, str)
    s3_obj = s3.Object(
        bucket, path)
    text = s3_obj.get()['Body'].read()
    return text


def save_df_to_s3_as_csv(df, bucket, path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, header=True, index=False)
    bucket.put_object(
        Key=check_path(path, str),
        Body=csv_buffer.getvalue())


def read_csv_from_s3(bucket, path):
    s3 = boto3.resource('s3')
    obj = s3.Bucket(bucket).Object(check_path(path, str))
    df = pd.read_csv(obj.get()['Body'])
    return df
