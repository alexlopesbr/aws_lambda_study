import json

from log import log


def lambda_handler(event, context):
    event_log = log(event)

    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from Lambda with GitHub Actions!\n Event log: {event_log}'),
    }
