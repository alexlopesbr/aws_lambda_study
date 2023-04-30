import boto3
import json

from s3Event import S3Event, S3Record


def lambda_handler(event, context):
    one_mega_byte = 1024 * 1024

    s3_client = boto3.client('s3')
    s3_records = event.get('Records')

    s3_event = S3Event([S3Record(**record) for record in s3_records])
    records = s3_event.records[0]

    bucket_name = records.s3.bucket.name
    object_key = records.s3.object.key

    get_object_response = s3_client.get_object(Bucket=bucket_name, Key=object_key)

    if get_object_response['ContentLength'] > one_mega_byte:
        raise Exception(f'File size is greater than {one_mega_byte} byte')

    print(f'File size is {get_object_response["ContentLength"]} bytes')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda with GitHub Actions!'),
    }
