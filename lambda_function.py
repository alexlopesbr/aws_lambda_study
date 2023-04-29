import boto3
import json

from log import log


def lambda_handler(event, context):
    one_mega_byte = 1024 * 1024
    s3_client = boto3.client('s3')

    event_log = log(event)
    record = event.Records[0]
    bucket = record.s3.bucket.name
    key = record.s3.object.key

    get_object_response = s3_client.get_object(bucket, key)

    if get_object_response['ContentLength'] > one_mega_byte:
        raise Exception(f'File size is greater than {one_mega_byte} byte')

    print(f'File size is {get_object_response["ContentLength"]} byte')

    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from Lambda with GitHub Actions!\n Event log: {event_log}'),
    }
